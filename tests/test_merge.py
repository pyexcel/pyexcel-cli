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
                                   file_fixture, dir_fixture, glob_fixture,
                                   output])
    eq_(result.exit_code, 0)
    expected = dedent("""
    .
    .
    .
    ---pyexcel:transcode_simple.csv---
    1,2,3
    ---pyexcel---
    ---pyexcel:merge_test.csv---
    1,2,3
    ---pyexcel---
    ---pyexcel:merge_test2.csv---
    1,2,3
    ---pyexcel---
    """).strip('\n') + '\n'
    eq_(result.output, expected)