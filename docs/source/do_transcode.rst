How to transcode a sheet of an excel file into csv
================================================================================

Suppose you have an example file as::

    >>> import pyexcel as p
	>>> bookdict = {
	...     "A": [[1]],
	...     "B": [[2]],
	...     "C": [[3]],
	... }
    >>> p.save_book_as(bookdict=bookdict, dest_file_name="example.xlsx")

Now, you would like to transcode sheet "B" into a csv file, you can do::

    $ pyexcel transcode --sheet-name B example.xslx example-sheet-b.csv


.. testcode::
   :hide:

   >>> import os
   >>> os.unlink('example.xlsx')
