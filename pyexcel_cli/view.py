"""
    pyexcel view
    ~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Onni Software Ltd.
    :license: MIT License, see LICENSE for more details

"""
import click
from pyexcel_cli.transcode import transcode


@click.command(short_help="View an excel file")
@click.option('--source-file-type')
@click.option('--output-file-type', default='texttable')
@click.argument('source')
@click.pass_context
def view(ctx, source_file_type, output_file_type, source):
    """
    Simply show the data inside the file

    \b
    SOURCE: a file name or '-'. '-' tells the command to use stdin
    """
    ctx.invoke(transcode,
               source_file_type=source_file_type,
               output_file_type=output_file_type,
               source=source,
               output='-')
