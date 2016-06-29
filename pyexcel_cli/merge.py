"""
    pyexcel merge
    ~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Onni Software Ltd.
    :license: MIT License, see LICENSE for more details

"""
import os
import csv
import sys
import glob
import click
from pyexcel.book import Book
from pyexcel import get_book


@click.command(short_help="Merge excel files into one")
@click.option('--output-file-type',
              help="file type of the stdout if '-' is given")
@click.option('--csv-delimiter', default=None)
@click.option('--csv-encoding', default=None)
@click.option('--csv-lineterminator', default=None)
@click.option('--csv-quotechar', default=None)
@click.option('--csv-escapechar', default=None)
@click.option('--csv-quoting', default=None)
@click.option('--csv-no-doublequote', default=False, is_flag=True)
@click.argument('sources', nargs=-1)
@click.argument('output', nargs=1)
def merge(output_file_type,
          csv_delimiter, csv_encoding, csv_quotechar,
          csv_escapechar, csv_quoting,
          csv_lineterminator, csv_no_doublequote,
          sources, output):
    """
    Merge excel files in various file formats into one excel file

    SOURCES: space separated parameters. a file name, a directory name
             or a file patterns
    OUTPUT: a file name or '-'. '-' tells the command to use stdout
    """
    file_list = []
    dir_list = []
    glob_list = []

    merged_book = Book()
    for source in sources:
        if os.path.isfile(source):
            file_list.append(source)
        elif os.path.isdir(source):
            dir_list.append(source)
        else:
            glob_list.append(source)

    params = {}
    if output_file_type == 'csv' or output.endswith('csv'):
        if csv_lineterminator is not None:
            params['lineterminator'] = csv_lineterminator
        if csv_encoding is not None:
            params['encoding'] = csv_encoding
        if csv_delimiter is not None:
            params['delimiter'] = _make_single_character(csv_delimiter)
        if csv_quotechar is not None:
            params['quotechar'] = _make_single_character(csv_quotechar)
        if csv_escapechar is not None:
            params['escapechar'] = _make_single_character(csv_escapechar)
        if csv_no_doublequote:
            params['no_doublequote'] = csv_no_doublequote
        if csv_quoting is None:
            params['quoting'] = csv.QUOTE_MINIMAL
        elif csv_quoting == 'none':
            params['quoting'] = csv.QUOTE_NONE
        elif csv_quoting == "all":
            params['quoting'] = csv.QUOTE_ALL
        elif csv_quoting == "nonnumeric":
            params['quoting'] = csv.QUOTE_NONNUMERIC

    for afile in _join_the_list(file_list, dir_list, glob_list):
        try:
            book = get_book(file_name=afile)
            merged_book += book
            if output != "-":
                click.echo(".")
        except NotImplementedError:
            click.echo("Skipping %s" % afile)
    if merged_book.number_of_sheets() > 0:
        if output == '-':
            merged_book.save_to_memory(output_file_type, sys.stdout, **params)
        else:
            merged_book.save_as(output, **params)
    else:
        click.echo("Nothing to be merged")


def _join_the_list(file_list, dir_list, glob_list):
    for afile in file_list:
        yield afile
    for directory in dir_list:
        for root, directories, files in os.walk(directory):
            for afile in files:
                yield os.path.join(root, afile)
    for globee in glob_list:
        for afile in glob.iglob(globee):
            yield afile


def _make_single_character(single_char_input):
    if sys.version_info[0] == 2:
        return single_char_input.encode('ascii')
    else:
        return single_char_input[0]
