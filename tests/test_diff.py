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


def test_difference():
    runner = CliRunner()
    test_fixture = os.path.join("tests", "fixtures", "transcode_simple.csv")
    test_fixture2 = os.path.join("tests", "fixtures", "multiple-sheets.xls")
    result = runner.invoke(diff, [test_fixture, test_fixture2])
    fixing = ""
    if os.name == "posix":
        fixing = " "
    expected = dedent("""
    --- tests{0}fixtures{0}transcode_simple.csv{1}

    +++ tests{0}fixtures{0}multiple-sheets.xls{1}

    @@ -1 +1,15 @@

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
    +---pyexcel---""").strip('\n') + '\n'
    eq_(result.output, expected.format(os.sep, fixing))
    eq_(result.exit_code, 1)
