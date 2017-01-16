"""
    pyexcel split
    ~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016-2017 by Onni Software Ltd.
    :license: MIT License, see LICENSE for more details

"""
import os
import click
from pyexcel_cli._shared import get_input_content
from pyexcel import get_book


@click.command(short_help="Split a multi-sheet file into single ones")
@click.option('--source-file-type',
              help="file type of the stdin if '-' as source")
@click.option('--output-file-type',
              help="file type of the splitted sheet")
@click.option('--output-dir',
              help="where to save the splitted files ")
@click.argument('source')
@click.argument('output_file_prefix')
def split(source_file_type, output_file_type,
          output_dir, source, output_file_prefix):
    """
    Split an excel file into one sheet per file

    \b
    SOURCE: a file name or '-'. '-' tells the command to use stdin
    OUTPUT_FILE_PREFIX: the splitted file name is form as
                        prefix_sheetname_index.file_type
    """
    params = {}
    if source == '-':
        params['file_content'] = get_input_content(source_file_type)
        params['file_type'] = source_file_type
    else:
        params['file_name'] = source
    book = get_book(**params)
    sheet_count = 0
    for sheet in book:
        file_name = "%s_%s_%d.%s" % (output_file_prefix, sheet.name,
                                     sheet_count, output_file_type)
        if output_dir is not None:
            file_name = os.path.join(output_dir, file_name)
        sheet.save_as(file_name)
        sheet_count += 1
