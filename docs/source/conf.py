# -*- coding: utf-8 -*-
DESCRIPTION = (
    'A command utility to read and write data in csv, tsv, xls, xlsx and od' +
    's format.' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

intersphinx_mapping = {
    'pyexcel': ('http://pyexcel.readthedocs.org/en/latest/', None),
}
spelling_word_list_filename = 'spelling_wordlist.txt'
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'pyexcel-cli'
copyright = u'2015-2017 Onni Software Ltd.'
version = '0.0.1'
release = '0.0.2'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'pyexcel-clidoc'
latex_elements = {}
latex_documents = [
    ('index', 'pyexcel-cli.tex',
     'pyexcel-cli Documentation',
     'Onni Software Ltd.', 'manual'),
]
man_pages = [
    ('index', 'pyexcel-cli',
     'pyexcel-cli Documentation',
     [u'Onni Software Ltd.'], 1)
]
texinfo_documents = [
    ('index', 'pyexcel-cli',
     'pyexcel-cli Documentation',
     'Onni Software Ltd.', 'pyexcel-cli',
     DESCRIPTION,
     'Miscellaneous'),
]
