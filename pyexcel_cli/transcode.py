"""
    pyexcel transcode
    ~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016-2017 by Onni Software Ltd.
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
@click.argument('source', nargs=1)
@click.argument('output', nargs=1)
def transcode(source_file_type, output_file_type,
              sheet_name, sheet_index,
              name_columns_by_row, name_rows_by_column,
              csv_source_delimiter, csv_source_encoding,
              csv_source_lineterminator, csv_source_quotechar,
              csv_source_escapechar, csv_source_quoting,
              csv_source_no_doublequote,
              csv_output_delimiter, csv_output_encoding,
              csv_output_lineterminator, csv_output_quotechar,
              csv_output_escapechar, csv_output_quoting,
              csv_output_no_doublequote,
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

    if source_file_type == 'csv' or source.endswith('csv'):
        csv_params = _make_csv_params(
            csv_source_lineterminator, csv_source_encoding,
            csv_source_delimiter, csv_source_quoting,
            csv_source_quotechar, csv_source_escapechar,
            csv_source_no_doublequote)
        params.update(csv_params)

    if output_file_type == 'csv' or output.endswith('csv'):
        csv_params = _make_csv_params(
            csv_output_lineterminator, csv_output_encoding,
            csv_output_delimiter, csv_output_quoting,
            csv_output_quotechar, csv_output_escapechar,
            csv_output_no_doublequote, prefix="dest_")
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
