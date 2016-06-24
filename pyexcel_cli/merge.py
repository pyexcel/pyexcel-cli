"""
    pyexcel merge
    ~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Onni Software Ltd.
    :license: MIT License, see LICENSE for more details

"""
import os
import sys
import glob
import click
from pyexcel.book import Book
from pyexcel import get_book


@click.command(short_help="Merge excel files into one")
@click.option('--output-file-type',
              help="file type of the stdout if '-' is given")
@click.argument('sources', nargs=-1)
@click.argument('output', nargs=1)
def merge(output_file_type, sources, output):
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

    for afile in _join_the_list(file_list, dir_list, glob_list):
        try:
            book = get_book(file_name=afile)
            merged_book += book
            click.echo(".")
        except NotImplementedError:
            click.echo("Skipping %s" % afile)
    if merged_book.number_of_sheets() > 0:
        if output == '-':
            merged_book.save_to_memory(output_file_type, sys.stdout)
        else:
            merged_book.save_as(output)
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
