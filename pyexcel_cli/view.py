"""
    pyexcel view
    ~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Onni Software Ltd.
    :license: MIT License, see LICENSE for more details

"""
import click
from pyexcel_cli.transcode import transcode


SHEET_TIP = "Once specified, it will work on pyexcel Sheet."


@click.command(short_help="View an excel file")
@click.option('--source-file-type')
@click.option('--output-file-type', default='texttable')
@click.option('--sheet-name',
              default=None,
              help="specify sheet name to operate on. " + SHEET_TIP)
@click.option('--sheet-index',
              default=None, type=int,
              help="specify sheet index to operate on. " + SHEET_TIP)
@click.option('--name-columns-by-row',
              default=None, type=int,
              help="use a row as column headers")
@click.option('--name-rows-by-column',
              default=None, type=int,
              help="use a column as row headers")
@click.option('--csv-source-delimiter', default=None)
@click.option('--csv-source-encoding', default=None)
@click.option('--csv-source-lineterminator', default=None)
@click.option('--csv-source-quotechar', default=None)
@click.option('--csv-source-escapechar', default=None)
@click.option('--csv-source-quoting', default=None)
@click.option('--csv-source-no-doublequote', default=False, is_flag=True)
@click.option('--csv-dest-delimiter', default=None)
@click.option('--csv-dest-encoding', default=None)
@click.option('--csv-dest-lineterminator', default=None)
@click.option('--csv-dest-quotechar', default=None)
@click.option('--csv-dest-escapechar', default=None)
@click.option('--csv-dest-quoting', default=None)
@click.option('--csv-dest-no-doublequote', default=False, is_flag=True)
@click.argument('source')
@click.pass_context
def view(ctx, **keywords):
    """
    Simply show the data inside the file

    \b
    SOURCE: a file name or '-'. '-' tells the command to use stdin
    """
    ctx.invoke(transcode, output='-', **keywords)
