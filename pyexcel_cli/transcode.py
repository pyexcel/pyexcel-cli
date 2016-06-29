"""
    pyexcel transcode
    ~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Onni Software Ltd.
    :license: MIT License, see LICENSE for more details

"""
import click
import pyexcel as pe

from pyexcel_cli._shared import (
    get_input_content,
    get_output_stream,
    _make_csv_params
)


SHEET_TIP = "Once specified, it will work on pyexcel Sheet."


@click.command(
    short_help="Transcode an excel file",
)
@click.option('--source-file-type',
              help="file type of the stdin if '-' as source")
@click.option('--output-file-type',
              help="file type of the stdout if '-' is given")
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
@click.option('--csv-quotechar', default=None)
@click.option('--csv-escapechar', default=None)
@click.option('--csv-quoting', default=None)
@click.option('--csv-no-doublequote', default=False, is_flag=True)
@click.argument('source', nargs=1)
@click.argument('output', nargs=1)
def transcode(source_file_type, output_file_type,
              sheet_name, sheet_index,
              name_columns_by_row, name_rows_by_column,
              csv_delimiter, csv_encoding,
              csv_lineterminator, csv_quotechar,
              csv_escapechar, csv_quoting,
              csv_no_doublequote,
              source, output):
    """
    Trancode an excel file from one format to another.

    \b
    SOURCE: a file name or '-'. '-' tells the command to use stdin
    OUTPUT: a file name or '-'. '-' tells the command to use stdout
    """
    params = {}
    if source == '-':
        params['file_content'] = get_input_content(source_file_type)
        params['file_type'] = source_file_type
    elif source.startswith("http"):
        params['url'] = source
    else:
        params['file_name'] = source
    if output == '-':
        params['dest_file_stream'] = get_output_stream(output_file_type)
        params['dest_file_type'] = output_file_type
    else:
        params['dest_file_name'] = output

    if output_file_type == 'csv' or output.endswith('csv'):
        csv_params = _make_csv_params(
            csv_lineterminator, csv_encoding, csv_delimiter,
            csv_quoting, csv_quotechar, csv_escapechar,
            csv_no_doublequote, prefix="dest_")
        params.update(csv_params)

    sheet_parameters = [sheet_name, sheet_index,
                        name_columns_by_row, name_rows_by_column]
    if _is_sheet_operation(sheet_parameters):
        if name_columns_by_row is not None:
            params['name_columns_by_row'] = name_columns_by_row
        elif name_rows_by_column is not None:
            params['name_rows_by_column'] = name_rows_by_column
        params['sheet_name'] = sheet_name
        params['sheet_index'] = sheet_index
        pe.save_as(**params)
    else:
        pe.save_book_as(**params)


def _is_sheet_operation(params):
    active_params = [element for element in params
                     if element is not None]
    return len(active_params) > 0
