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
@click.option('--csv-delimiter', default=None)
@click.option('--csv-encoding', default=None)
@click.option('--csv-lineterminator', default=None)
@click.option('--csv-no-doublequote', default=False, is_flag=True)
@click.argument('source')
@click.pass_context
def view(ctx, source_file_type, output_file_type,
         sheet_name, sheet_index,
         name_columns_by_row, name_rows_by_column,
         csv_delimiter, csv_encoding,
         csv_lineterminator, csv_no_doublequote,
         source):
    """
    Simply show the data inside the file

    \b
    SOURCE: a file name or '-'. '-' tells the command to use stdin
    """
    ctx.invoke(transcode,
               source_file_type=source_file_type,
               output_file_type=output_file_type,
               source=source,
               sheet_name=sheet_name,
               sheet_index=sheet_index,
               name_columns_by_row=name_columns_by_row,
               name_rows_by_column=name_rows_by_column,
               csv_delimiter=csv_delimiter,
               csv_encoding=csv_encoding,
               csv_lineterminator=csv_lineterminator,
               csv_no_doublequote=csv_no_doublequote,
               output='-')
