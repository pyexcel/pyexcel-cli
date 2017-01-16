"""
    pyexcel diff
    ~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016-2017 by Onni Software Ltd.
    :license: MIT License, see LICENSE for more details

"""
import sys
import click
import pyexcel as pe
from difflib import unified_diff

from pyexcel_cli._shared import get_input_content


@click.command(short_help="diff two excel files")
@click.option('--source-file-type',
              help="file type of the stdin if '-' as source")
@click.option('--file-type', default='csv',
              help="the basis where two files are compared")
@click.argument('source')
@click.argument('dest')
def diff(source_file_type, file_type, source, dest):
    """
    Find difference in plain data format

    Both files are transcoded into a file stream of a common file type.
    Then a diff operation is run on them.

    \b
    SOURCE: a file name or '-'. '-' tells the command to use stdin
    DEST: a file name
    """
    params = {}
    if source == '-':
        params['file_content'] = get_input_content(source_file_type)
        params['file_type'] = source_file_type
    else:
        params['file_name'] = source
    params['dest_file_type'] = file_type
    source_lines = pe.save_book_as(**params)
    dest_lines = pe.save_book_as(file_name=dest,
                                 dest_file_type=file_type)
    result = unified_diff(source_lines.getvalue().splitlines(),
                          dest_lines.getvalue().splitlines(),
                          source, dest)
    has_difference = 0
    for difference in result:
        has_difference = 1
        click.echo(difference)
    sys.exit(has_difference)
