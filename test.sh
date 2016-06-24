pip freeze
nosetests --with-cov --cover-package pyexcel_cli --cover-package tests --with-doctest --doctest-extension=.rst tests README.rst pyexcel_cli  && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
