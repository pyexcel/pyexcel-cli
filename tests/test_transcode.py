import os
from nose.tools import eq_
from pyexcel_cli.transcode import transcode
from click.testing import CliRunner


def test_simple_option():
    runner = CliRunner()
    test_fixture = os.path.join("tests", "fixtures",
                                "transcode_simple.csv")
    output = "test_simple_option.csv"
    result = runner.invoke(transcode, ["--csv-lineterminator", "\n",
                                       test_fixture, output])
    print(result.output)
    eq_(result.exit_code, 0)
    with open(output, 'r') as f:
        content = f.read()
        eq_(content, '1,2,3\n')
    os.unlink(output)


def test_stdout_option():
    runner = CliRunner()
    test_fixture = os.path.join("tests", "fixtures",
                                "transcode_simple.csv")
    result = runner.invoke(transcode, ["--output-file-type", "csv",
                                       test_fixture, '-'])
    eq_(result.exit_code, 0)
    eq_(result.output, '1,2,3\n')


def test_stdin_option():
    runner = CliRunner()
    result = runner.invoke(transcode,
                           ["--source-file-type", "csv",
                            "--output-file-type", "csv", '-', '-'],
                           input='1,2,3')
    eq_(result.output, '1,2,3\n')
    eq_(result.exit_code, 0)


def test_name_columns_by_row():
    runner = CliRunner()
    test_fixture = os.path.join("tests", "fixtures",
                                "transcode_headers.csv")
    result = runner.invoke(transcode, ["--output-file-type", "json",
                                       "--name-columns-by-row",  "0",
                                       test_fixture, '-'])
    eq_(result.exit_code, 0)
    expected = ('{"transcode_headers.csv": ' +
                '[{"grade": 100, "name": "Adam"}, ' +
                '{"grade": 100, "name": "Eve"}]}')
    eq_(result.output, expected)


def test_multiple_sheet():
    runner = CliRunner()
    test_fixture = os.path.join("tests", "fixtures",
                                "multiple-sheets.xls")
    result = runner.invoke(transcode, ["--output-file-type", "json",
                                       "--name-columns-by-row",  "0",
                                       "--sheet-name", "Sheet 3",
                                       test_fixture, '-'])
    eq_(result.exit_code, 0)
    expected = ('{"Sheet 3": [{"O": 3, "P": 2, "Q": 1}, ' +
                '{"O": 4, "P": 3, "Q": 2}]}')
    eq_(result.output, expected)


def test_multiple_sheet_by_index():
    runner = CliRunner()
    test_fixture = os.path.join("tests", "fixtures",
                                "multiple-sheets.xls")
    result = runner.invoke(transcode, ["--output-file-type", "json",
                                       "--name-columns-by-row",  "0",
                                       "--sheet-index", "2",
                                       test_fixture, '-'])
    eq_(result.exit_code, 0)
    expected = ('{"Sheet 3": [{"O": 3, "P": 2, "Q": 1}, ' +
                '{"O": 4, "P": 3, "Q": 2}]}')
    eq_(result.output, expected)
