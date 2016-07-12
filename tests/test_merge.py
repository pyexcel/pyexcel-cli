import os
from nose.tools import eq_
from pyexcel_cli.merge import merge
from click.testing import CliRunner
from pyexcel import get_book
from textwrap import dedent


def test_simple_option():
    runner = CliRunner()
    file_fixture = os.path.join("tests", "fixtures", "transcode_simple.csv")
    dir_fixture = os.path.join("tests", "fixtures", "file_dir")
    glob_fixture = os.path.join("tests", "fixtures", "glob_dir", "*")
    output = "test_simple_option.xls"
    result = runner.invoke(merge, [file_fixture, dir_fixture, glob_fixture,
                                   output])
    eq_(result.exit_code, 0)
    book = get_book(file_name=output)
    expected = dedent("""
    transcode_simple.csv:
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
    merge_test.csv:
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
    merge_test2.csv:
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+""").strip('\n')
    eq_(str(book), expected)
    os.unlink(output)


def test_stdout_option():
    runner = CliRunner()
    file_fixture = os.path.join("tests", "fixtures", "transcode_simple.csv")
    dir_fixture = os.path.join("tests", "fixtures", "file_dir")
    glob_fixture = os.path.join("tests", "fixtures", "glob_dir", "*")
    output = "-"
    result = runner.invoke(merge, ["--output-file-type", "csv",
                                   "--csv-output-lineterminator", "\n",
                                   "--csv-output-delimiter", ";",
                                   file_fixture, dir_fixture, glob_fixture,
                                   output])
    eq_(result.exit_code, 0)
    expected = dedent("""
    ---pyexcel:transcode_simple.csv---
    1;2;3
    ---pyexcel---
    ---pyexcel:merge_test.csv---
    1;2;3
    ---pyexcel---
    ---pyexcel:merge_test2.csv---
    1;2;3
    ---pyexcel---
    """).strip('\n') + '\n'
    eq_(result.output, expected)


def test_more_csv_options():
    runner = CliRunner()
    file_fixture = os.path.join("tests", "fixtures", "transcode_quoted.csv")
    output = "-"
    result = runner.invoke(merge, ["--output-file-type", "csv",
                                   "--csv-output-lineterminator", "\n",
                                   "--csv-output-delimiter", ":",
                                   "--csv-output-quoting", "minimal",
                                   file_fixture, output])
    eq_(result.exit_code, 0)
    expected = dedent("""
    hello:|world|:1:2
    3:4:5:6
    """).strip('\n') + '\n'
    eq_(result.output, expected)


def test_nothing_do_do():
    runner = CliRunner()
    glob_fixture = os.path.join("tests", "fixtures", "nothing_is_excel", "*")
    output = "test_simple_option.xls"
    result = runner.invoke(merge, [glob_fixture, output])
    expected = dedent("""
    Skipping tests{0}fixtures{0}nothing_is_excel{0}test.no.excel
    Nothing to be merged""").strip('\n') + '\n'
    eq_(result.exit_code, 0)
    eq_(result.output, expected.format(os.sep))
