import os
from nose.tools import eq_
from pyexcel_cli.view import view
from click.testing import CliRunner


def test_stdin_option():
    runner = CliRunner()
    result = runner.invoke(view,
                           ["--source-file-type", "csv",
                            "--output-file-type", "csv", '-'],
                           input='1,2,3')
    eq_(result.output, '1,2,3\n')
    eq_(result.exit_code, 0)


def test_stdout_option():
    runner = CliRunner()
    test_fixture = os.path.join("tests", "fixtures", "transcode_simple.csv")
    result = runner.invoke(view, ["--output-file-type", "csv",
                                  test_fixture])
    eq_(result.exit_code, 0)
    eq_(result.output, '1,2,3\n')
