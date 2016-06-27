import click
from pyexcel.core import get_io_type


def get_input_content(file_type):
    stream = get_stream('stdin', file_type)
    content = stream.read()
    return content


def get_output_stream(file_type):
    return get_stream('stdout', file_type)


def get_stream(name, file_type):
    stream = None
    stream_type = get_io_type(file_type)
    if stream_type == "string":
        stream = click.get_text_stream(name)
    else:
        stream = click.get_binary_stream(name)

    return stream
