`pyexcel-cli` - Let you focus on data, instead of file formats
================================================================================

:Author: C.W.
:Source code: http://github.com/pyexcel/pyexcel-cli.git
:Issues: http://github.com/pyexcel/pyexcel-cli/issues
:License: New BSD License
:Development: |release|
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

Here is an example usage:

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
You can install it via pip:

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

   ======================== ======================= =============== ==================
   Package name              Supported file formats  Dependencies   Python versions
   ======================== ======================= =============== ==================
   `pyexcel-io`_            csv, csvz [#f1]_, tsv,                  2.6, 2.7, 3.3,
                            tsvz [#f2]_                             3.4, 3.5, 3.6
                                                                    pypy
   `pyexcel-xls`_           xls, xlsx(read only),   `xlrd`_,        same as above
                            xlsm(read only)         `xlwt`_
   `pyexcel-xlsx`_          xlsx                    `openpyxl`_     same as above
   `pyexcel-xlsxw`_         xlsx(write only)        `XlsxWriter`_   same as above
   `pyexcel-ods3`_          ods                     `ezodf`_,       2.6, 2.7, 3.3, 3.4
                                                    lxml            3.5, 3.6
   `pyexcel-ods`_           ods                     `odfpy`_        same as above
   `pyexcel-odsr`_          ods(read only)          lxml            same as above
   `pyexcel-text`_          (write only)json, rst,  `tabulate`_     2.6, 2.7, 3.3, 3.4
                            mediawiki, html,                        3.5, pypy, pypy3
                            latex, grid, pipe,
                            orgtbl, plain simple
   `pyexcel-handsontable`_  handsontable in html    `handsontable`_ same as above [#f3]_
   `pyexcel-pygal`_         svg chart               `pygal`_        same as above [#f3]_
   ======================== ======================= =============== ==================

.. _pyexcel-io: https://github.com/pyexcel/pyexcel-io
.. _pyexcel-xls: https://github.com/pyexcel/pyexcel-xls
.. _pyexcel-xlsx: https://github.com/pyexcel/pyexcel-xlsx
.. _pyexcel-ods: https://github.com/pyexcel/pyexcel-ods
.. _pyexcel-ods3: https://github.com/pyexcel/pyexcel-ods3
.. _pyexcel-odsr: https://github.com/pyexcel/pyexcel-odsr
.. _pyexcel-xlsxw: https://github.com/pyexcel/pyexcel-xlsxw

.. _xlrd: https://github.com/python-excel/xlrd
.. _xlwt: https://github.com/python-excel/xlwt
.. _openpyxl: https://bitbucket.org/openpyxl/openpyxl
.. _XlsxWriter: https://github.com/jmcnamara/XlsxWriter
.. _ezodf: https://github.com/T0ha/ezodf
.. _odfpy: https://github.com/eea/odfpy

.. _pyexcel-text: https://github.com/pyexcel/pyexcel-text
.. _tabulate: https://bitbucket.org/astanin/python-tabulate
.. _pyexcel-handsontable: https://github.com/pyexcel/pyexcel-handsontable
.. _handsontable: https://cdnjs.com/libraries/handsontable
.. _pyexcel-pygal: https://github.com/pyexcel/pyexcel-chart
.. _pygal: https://github.com/Kozea/pygal
.. _pyexcel-matplotlib: https://github.com/pyexcel/pyexcel-matplotlib
.. _matplotlib: https://matplotlib.org

.. [#f3] coming soon

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