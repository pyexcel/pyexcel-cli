`pyexcel-cli` - Let you focus on data, instead of file formats
================================================================================

:Author: C.W.
:Source code: http://github.com/pyexcel/pyexcel-cli.git
:Issues: http://github.com/pyexcel/pyexcel-cli/issues
:License: New BSD License
:Development: |version|
:Released: |release|
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

Recently, pyexcel(0.2.2+) and its plugins(0.2.0+) started using newer version of setuptools. Please upgrade your setup tools before install latest pyexcel components:

.. code-block:: bash

    $ pip install --upgrade setuptools

You can install it via pip:

.. code-block:: bash

    $ pip install pyexcel-cli


or clone it and install it:

.. code-block:: bash

    $ git clone http://github.com/pyexcel/pyexcel-cli.git
    $ cd pyexcel-cli
    $ python setup.py install


List of plugins
================================================================================

.. _file-format-list:

.. table:: A list of file formats supported by external plugins

   ================ ========================================
   Plugins          Supported file formats
   ================ ========================================
   `pyexcel-xls`_   xls, xlsx(r), xlsm(r)
   `pyexcel-xlsx`_  xlsx
   `pyexcel-ods3`_  ods (python 2.6, 2.7, 3.3, 3.4)
   `pyexcel-ods`_   ods (python 2.6, 2.7)
   `pyexcel-text`_  (write only)json, rst, mediawiki, html
                    latex, grid, pipe, orgtbl, plain simple
   ================ ========================================

.. _pyexcel-xls: https://github.com/pyexcel/pyexcel-xls
.. _pyexcel-xlsx: https://github.com/pyexcel/pyexcel-xlsx
.. _pyexcel-ods: https://github.com/pyexcel/pyexcel-ods
.. _pyexcel-ods3: https://github.com/pyexcel/pyexcel-ods3
.. _pyexcel-text: https://github.com/pyexcel/pyexcel-text

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