`pyexcel-cli` - Let you focus on data, instead of file formats
================================================================================

:Author: C.W.
:Source code: http://github.com/pyexcel/pyexcel-cli.git
:Issues: http://github.com/pyexcel/pyexcel-cli/issues
:License: New BSD License
:Released: |version|
:Generated: |today|

Introduction
================================================================================

**pyexcel-cli** brings `pyexcel <https://github.com/pyexcel/pyexcel>`_ to make it easy
to consume/produce information stored in excel files on command line interface.
This library can turn the excel data into a list of lists, a list of records(dictionaries),
dictionaries of lists. And vice versa. Hence it lets you focus on data in shell
programming, instead of file formats.

Hightlighted features:

#. View data in the excel files without Microsoft Office or Open Office
#. Transcode data among supported excel file formats
#. Merge files in various excel file formats into one
#. Split a multi-sheet excel file into single sheet files
#. Find difference in data between two excel files

Usage
================================================================================

.. code-block:: bash

   $ cd demo
   $ pyexcel view --in-browser --output-file-type sortable.html --sheet-index 0 https://github.com/pyexcel/excel2table/raw/master/sample/goog.ods

Here's what you will get:

.. image:: https://github.com/pyexcel/pyexcel-cli/raw/master/pyexcel-cli-sortable.gif

.. note::

   You will need to install pyexcel-sortable, which renders it.

Here is another cli example usage:

.. code-block:: bash

    $ pyexcel view https://github.com/pyexcel/pyexcel-cli/blob/master/tests/fixtures/multiple-sheets.xls
    Sheet 1:
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    Sheet 2:
    +---+---+---+
    | X | Y | Z |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    Sheet 3:
    +---+---+---+
    | O | P | Q |
    +---+---+---+
    | 3 | 2 | 1 |
    +---+---+---+
    | 4 | 3 | 2 |
    +---+---+---+

Because pyexcel family is loosely coupled, especially for file format supports, you
install the libraries that you need to. If you need to support xls format, you will
need to install pyexcel-xls. For more information, please see the plugin section.


Installation
================================================================================

You can install pyexcel-cli via pip:

.. code-block:: bash

    $ pip install pyexcel-cli


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/pyexcel/pyexcel-cli.git
    $ cd pyexcel-cli
    $ python setup.py install


List of plugins
================================================================================

.. _file-format-list:
.. _a-map-of-plugins-and-file-formats:

.. table:: A list of file formats supported by external plugins

   ======================== ======================= ================= ==================
   Package name              Supported file formats  Dependencies     Python versions
   ======================== ======================= ================= ==================
   `pyexcel-io`_            csv, csvz [#f1]_, tsv,                    2.6, 2.7, 3.3,
                            tsvz [#f2]_                               3.4, 3.5, 3.6
                                                                      pypy
   `pyexcel-xls`_           xls, xlsx(read only),   `xlrd`_,          same as above
                            xlsm(read only)         `xlwt`_
   `pyexcel-xlsx`_          xlsx                    `openpyxl`_       same as above
   `pyexcel-ods3`_          ods                     `pyexcel-ezodf`_, 2.6, 2.7, 3.3, 3.4
                                                    lxml              3.5, 3.6
   `pyexcel-ods`_           ods                     `odfpy`_          same as above
   ======================== ======================= ================= ==================

.. table:: Dedicated file reader and writers

   ======================== ======================= ================= ==================
   Package name              Supported file formats  Dependencies     Python versions
   ======================== ======================= ================= ==================
   `pyexcel-xlsxw`_         xlsx(write only)        `XlsxWriter`_     Python 2 and 3
   `pyexcel-xlsxr`_         xlsx(read only)         lxml              same as above
   `pyexcel-xlsbr`_         xlsx(read only)         pyxlsb            same as above
   `pyexcel-odsr`_          read only for ods, fods lxml              same as above
   `pyexcel-odsw`_          write only for ods      loxun             same as above
   `pyexcel-htmlr`_         html(read only)         lxml,html5lib     same as above
   `pyexcel-pdfr`_          pdf(read only)          pdftables         Python 2 only.
   ======================== ======================= ================= ==================


.. _pyexcel-io: https://github.com/pyexcel/pyexcel-io
.. _pyexcel-xls: https://github.com/pyexcel/pyexcel-xls
.. _pyexcel-xlsx: https://github.com/pyexcel/pyexcel-xlsx
.. _pyexcel-ods: https://github.com/pyexcel/pyexcel-ods
.. _pyexcel-ods3: https://github.com/pyexcel/pyexcel-ods3
.. _pyexcel-odsr: https://github.com/pyexcel/pyexcel-odsr
.. _pyexcel-odsw: https://github.com/pyexcel/pyexcel-odsw
.. _pyexcel-pdfr: https://github.com/pyexcel/pyexcel-pdfr

.. _pyexcel-xlsxw: https://github.com/pyexcel/pyexcel-xlsxw
.. _pyexcel-xlsxr: https://github.com/pyexcel/pyexcel-xlsxr
.. _pyexcel-xlsbr: https://github.com/pyexcel/pyexcel-xlsbr
.. _pyexcel-htmlr: https://github.com/pyexcel/pyexcel-htmlr

.. _xlrd: https://github.com/python-excel/xlrd
.. _xlwt: https://github.com/python-excel/xlwt
.. _openpyxl: https://bitbucket.org/openpyxl/openpyxl
.. _XlsxWriter: https://github.com/jmcnamara/XlsxWriter
.. _pyexcel-ezodf: https://github.com/pyexcel/pyexcel-ezodf
.. _odfpy: https://github.com/eea/odfpy

.. table:: Other data renderers

   ======================== ======================= ================= ==================
   Package name              Supported file formats  Dependencies     Python versions
   ======================== ======================= ================= ==================
   `pyexcel-text`_          write only:rst,         `tabulate`_       2.6, 2.7, 3.3, 3.4
                            mediawiki, html,                          3.5, 3.6, pypy
                            latex, grid, pipe,
                            orgtbl, plain simple
                            read only: ndjson
                            r/w: json
   `pyexcel-handsontable`_  handsontable in html    `handsontable`_   same as above
   `pyexcel-pygal`_         svg chart               `pygal`_          2.7, 3.3, 3.4, 3.5
                                                                      3.6, pypy
   `pyexcel-sortable`_      sortable table in html  `csvtotable`_     same as above
   `pyexcel-gantt`_         gantt chart in html     `frappe-gantt`_   except pypy, same
                                                                      as above
   ======================== ======================= ================= ==================

.. _pyexcel-text: https://github.com/pyexcel/pyexcel-text
.. _tabulate: https://bitbucket.org/astanin/python-tabulate
.. _pyexcel-handsontable: https://github.com/pyexcel/pyexcel-handsontable
.. _handsontable: https://cdnjs.com/libraries/handsontable
.. _pyexcel-pygal: https://github.com/pyexcel/pyexcel-chart
.. _pygal: https://github.com/Kozea/pygal
.. _pyexcel-matplotlib: https://github.com/pyexcel/pyexcel-matplotlib
.. _matplotlib: https://matplotlib.org
.. _pyexcel-sortable: https://github.com/pyexcel/pyexcel-sortable
.. _csvtotable: https://github.com/vividvilla/csvtotable
.. _pyexcel-gantt: https://github.com/pyexcel/pyexcel-gantt
.. _frappe-gantt: https://github.com/frappe/gantt

In order to manage the list of plugins installed, you need to use pip to add or remove
a plugin. When you use virtualenv, you can have different plugins per virtual
environment. In the situation where you have multiple plugins that does the same thing
in your environment, you need to tell pyexcel which plugin to use per function call.
For example, pyexcel-ods and pyexcel-odsr, and you want to get_array to use pyexcel-odsr.
You need to append get_array(..., library='pyexcel-odsr').

.. rubric:: Footnotes

.. [#f1] zipped csv file
.. [#f2] zipped tsv file

Command line reference
================================================================================

Usage: pyexcel-script.py [OPTIONS] COMMAND [ARGS]...

  Read and write data in different excel formats

  file type in pyexcel refers to file formats, e.g. csv, xls

Options:
  --help  Show this message and exit.

Commands:
  #. diff       diff two excel files
  #. merge      Merge excel files into one
  #. split      Split a multi-sheet file into single ones
  #. transcode  Transcode an excel file
  #. view       View an excel file

Tutorial
================================================================================

.. toctree::

   do_diff
   do_transcode
   do_view