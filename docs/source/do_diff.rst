How to see the difference between two excel files using pyexcel-cli
================================================================================

First of all, the difference in fonts, styles, formula and charts are not
supported. It only finds the difference in data. In order to see all
command line options, you could do::

    $ pyexcel diff --help

In order to get you started, here is an example command line::

    $ pyexcel diff filea.xls fileb.csv

The source file content could come from stdin, but the command line syntax
changes a bit::

    $ cat filea.xls | pyexcel diff --source-file-type xls - fileb.csv
