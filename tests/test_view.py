#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from nose.tools import eq_
from pyexcel_cli.view import view
from click.testing import CliRunner
from textwrap import dedent


def test_stdin_option():
    runner = CliRunner()
    result = runner.invoke(view,
                           ["--source-file-type", "csv",
                            "--csv-output-lineterminator", "\n",
                            "--output-file-type", "csv", '-'],
                           input='1,2,3')
    eq_(result.output, '1,2,3\n')
    eq_(result.exit_code, 0)


def test_stdout_option():
    runner = CliRunner()
    test_fixture = os.path.join("tests", "fixtures", "transcode_simple.csv")
    result = runner.invoke(view, ["--output-file-type", "csv",
                                  "--csv-output-lineterminator", "\n",
                                  test_fixture])
    eq_(result.exit_code, 0)
    eq_(result.output, '1,2,3\n')


def test_csv_encoding_option():
    runner = CliRunner()
    test_fixture = os.path.join("tests", "fixtures", "csv-encoding-utf16.csv")
    result = runner.invoke(view, ["--output-file-type", "csv",
                                  "--csv-source-encoding", "utf-16",
                                  "--csv-output-lineterminator", "\n",
                                  test_fixture])
    eq_(result.exit_code, 0)
    if sys.version_info[0] == 2:
        output = result.output.encode('utf-8')
    else:
        output = result.output
    eq_(output, 'Äkkilähdöt,Matkakirjoituksia,Matkatoimistot\n')


def test_url_option():
    runner = CliRunner()
    test_fixture = "https://github.com/pyexcel/pyexcel-cli/raw/master/tests/fixtures/multiple-sheets.xls"  # noqa
    result = runner.invoke(view, [test_fixture])
    expected = dedent("""
    Sheet 1:
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    Sheet 2:
    +---+---+---+
    | X | Y | Z |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    Sheet 3:
    +---+---+---+
    | O | P | Q |
    +---+---+---+
    | 3 | 2 | 1 |
    +---+---+---+
    | 4 | 3 | 2 |
    +---+---+---+
    """).strip('\n')
    eq_(result.exit_code, 0)
    eq_(result.output, expected)
