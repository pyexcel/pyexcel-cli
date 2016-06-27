import os
from nose.tools import eq_
from pyexcel_cli.split import split
from click.testing import CliRunner
from pyexcel import get_book, get_sheet


def test_simple_option():
    runner = CliRunner()
    file_fixture = os.path.join("tests", "fixtures", "multiple-sheets.xls")
    prefix = "output"
    result = runner.invoke(split, ['--output-file-type', 'xlsx',
                                   file_fixture, prefix])
    eq_(result.exit_code, 0)
    book = get_book(file_name=file_fixture)
    count = 0
    for sheet in book:
        splitted_file = "%s_%s_%s.xlsx" % (prefix, sheet.name, count)
        count += 1
        written_sheet = get_sheet(file_name=splitted_file)
        eq_(str(sheet), str(written_sheet))
        os.unlink(splitted_file)


def test_stdin_option():
    runner = CliRunner()
    file_fixture = os.path.join("tests", "fixtures", "multiple-sheets.xls")
    input_stream = open(file_fixture, "rb")
    prefix = "output"
    result = runner.invoke(split,
                           ['--source-file-type', "xls",
                            '--output-file-type', 'xlsx',
                            '-', prefix],
                           input=input_stream.read())
    eq_(result.exit_code, 0)
    book = get_book(file_name=file_fixture)
    count = 0
    for sheet in book:
        splitted_file = "%s_%s_%s.xlsx" % (prefix, sheet.name, count)
        count += 1
        written_sheet = get_sheet(file_name=splitted_file)
        eq_(str(sheet), str(written_sheet))
        os.unlink(splitted_file)
    input_stream.close()
