import sys
import csv
import click
from pyexcel.core import get_io_type


def get_input_content(file_type):
    if sys.version_info[0] == 2:
        stream = sys.stdin
    else:
        stream = get_stream('stdin', file_type)
    content = stream.read()
    return content


def get_output_stream(file_type):
    if sys.version_info[0] == 2:
        return sys.stdout
    else:
        return get_stream('stdout', file_type)


def get_stream(name, file_type):
    stream = None
    stream_type = get_io_type(file_type)
    if stream_type == "string":
        stream = click.get_text_stream(name)
    else:
        stream = click.get_binary_stream(name)

    return stream


def _make_single_character(single_char_input):
    if sys.version_info[0] == 2:
        return single_char_input.encode('ascii')
    else:
        return single_char_input[0]


def _make_csv_params(lineterminator,
                     encoding,
                     delimiter,
                     quoting,
                     quotechar,
                     escapechar,
                     no_doublequote, prefix=""):
    params = {}
    if lineterminator is not None:
        params[prefix + 'lineterminator'] = lineterminator
    if encoding is not None:
        params[prefix + 'encoding'] = encoding
    if delimiter is not None:
        params[prefix + 'delimiter'] = _make_single_character(delimiter)
    if quotechar is not None:
        params[prefix + 'quotechar'] = _make_single_character(quotechar)
    if escapechar is not None:
        params[prefix + 'escapechar'] = _make_single_character(escapechar)
    if no_doublequote:
        params[prefix + 'no_doublequote'] = no_doublequote
    if quoting is None:
        params[prefix + 'quoting'] = csv.QUOTE_MINIMAL
    elif quoting == 'none':
        params[prefix + 'quoting'] = csv.QUOTE_NONE
    elif quoting == "all":
        params[prefix + 'quoting'] = csv.QUOTE_ALL
    elif quoting == "nonnumeric":
        params[prefix + 'quoting'] = csv.QUOTE_NONNUMERIC
    return params
