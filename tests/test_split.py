import os
from nose.tools import eq_
from pyexcel_cli.split import split
from click.testing import CliRunner
from pyexcel import get_book, get_sheet


def test_simple_option():
    runner = CliRunner()
    file_fixture = os.path.join("tests", "fixtures", "multiple-sheets.xls")
    prefix = "output"
    runner.invoke(split, ['--output-file-type', 'ods',
                          file_fixture, prefix])
    book = get_book(file_name=file_fixture)
    count = 0
    for sheet in book:
        splitted_file = "%s_%s_%s.ods" % (prefix, sheet.name, count)
        count += 1
        written_sheet = get_sheet(file_name=splitted_file)
        eq_(str(sheet), str(written_sheet))
        os.unlink(splitted_file)
