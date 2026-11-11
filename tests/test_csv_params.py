import os

import click
import pytest
from click.testing import CliRunner

from pyexcel_cli._shared import _make_single_character
from pyexcel_cli.transcode import transcode


def test_single_character_pass_through():
    assert _make_single_character(";") == ";"


def test_empty_character_is_rejected():
    with pytest.raises(click.BadParameter):
        _make_single_character("")


def test_multi_character_is_rejected():
    with pytest.raises(click.BadParameter):
        _make_single_character(";;")


def test_transcode_empty_delimiter_is_clean_error():
    runner = CliRunner()
    file_fixture = os.path.join("tests", "fixtures", "transcode_simple.csv")
    result = runner.invoke(transcode, ["--csv-source-delimiter", "",
                                       file_fixture, "unused_out.csv"])
    assert result.exit_code == 2
    assert not isinstance(result.exception, IndexError)
