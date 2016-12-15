"""
    pyexcel_cli
    ~~~~~~~~~~~~~~~~~~~

    command line interface for pyexcel

    :copyright: (c) 2016 by Onni Software Ltd.
    :license: MIT License, see LICENSE for more details

"""
import click

from pyexcel_cli.diff import diff
from pyexcel_cli.view import view
from pyexcel_cli.split import split
from pyexcel_cli.merge import merge
from pyexcel_cli.transcode import transcode


@click.group()
def main():
    """
    Read and write data in different excel formats

    file type in pyexcel refers to file formats, e.g. csv, xls
    """
    pass


main.add_command(transcode)
main.add_command(merge)
main.add_command(split)
main.add_command(view)
main.add_command(diff)
