isort $(find pyexcel_cli -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
black -l 79 pyexcel_cli
black -l 79 tests
