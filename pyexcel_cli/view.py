"""
    pyexcel view
    ~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016-2017 by Onni Software Ltd.
    :license: MIT License, see LICENSE for more details

"""
import click
from pyexcel_cli.transcode import transcode
import tempfile


SHEET_TIP = "Once specified, it will work on pyexcel Sheet."


@click.command(short_help="View an excel file")
@click.option('--in-browser', '-b', is_flag=True,
              help="View the excel file in a browser")
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
@click.option('--csv-output-delimiter', default=None)
@click.option('--csv-output-encoding', default=None)
@click.option('--csv-output-lineterminator', default=None)
@click.option('--csv-output-quotechar', default=None)
@click.option('--csv-output-escapechar', default=None)
@click.option('--csv-output-quoting', default=None)
@click.option('--csv-output-no-doublequote', default=False, is_flag=True)
@click.argument('source')
@click.pass_context
def view(ctx, in_browser, **keywords):
    """
    Simply show the data inside the file

    \b
    SOURCE: a file name or '-'. '-' tells the command to use stdin
    """
    output = '-'
    if in_browser:
        output = tempfile.mkstemp(suffix='handsontable.html')[1]
    ctx.invoke(transcode, output=output, **keywords)
    if in_browser:
        import webbrowser
        webbrowser.open("file://" + output)
