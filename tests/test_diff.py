import os
from nose.tools import eq_
from pyexcel_cli.diff import diff
from click.testing import CliRunner
from textwrap import dedent


def test_no_difference():
    runner = CliRunner()
    test_fixture = os.path.join("tests", "fixtures", "transcode_simple.csv")
    result = runner.invoke(diff, [test_fixture, test_fixture])
    eq_(result.output, '')  # no difference
    eq_(result.exit_code, 0)


def test_stdin_option():
    runner = CliRunner()
    test_fixture2 = os.path.join("tests", "fixtures", "multiple-sheets.xls")
    result = runner.invoke(diff,
                           ["--source-file-type", "csv",
                            "-", test_fixture2],
                           input='1,2,3')
    body = dedent("""
    +---pyexcel:Sheet 1---
     1,2,3
    +4,5,6
    +7,8,9
    +---pyexcel---
    +---pyexcel:Sheet 2---
    +X,Y,Z
    +1,2,3
    +4,5,6
    +---pyexcel---
    +---pyexcel:Sheet 3---
    +O,P,Q
    +3,2,1
    +4,3,2
    +---pyexcel---
    """)
    assert result.output.endswith(body)
    eq_(result.exit_code, 1)


def test_difference():
    runner = CliRunner()
    test_fixture = os.path.join("tests", "fixtures", "transcode_simple.csv")
    test_fixture2 = os.path.join("tests", "fixtures", "multiple-sheets.xls")
    result = runner.invoke(diff, [test_fixture, test_fixture2])
    body = dedent("""
    +---pyexcel:Sheet 1---
     1,2,3
    +4,5,6
    +7,8,9
    +---pyexcel---
    +---pyexcel:Sheet 2---
    +X,Y,Z
    +1,2,3
    +4,5,6
    +---pyexcel---
    +---pyexcel:Sheet 3---
    +O,P,Q
    +3,2,1
    +4,3,2
    +---pyexcel---
    """)
    assert result.output.endswith(body)
    eq_(result.exit_code, 1)
