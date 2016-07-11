try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

NAME = 'pyexcel-cli'
AUTHOR = 'C.W.'
VERSION = '0.0.1'
EMAIL = 'wangc_2011 (at) hotmail.com'
LICENSE = 'New BSD'
ENTRY_POINTS = {
    'console_scripts': [
        'pyexcel = pyexcel_cli.main:main'
    ]
}
PACKAGES = find_packages(exclude=['ez_setup', 'examples', 'tests'])
DESCRIPTION = (
    'A command utility to read and write data in csv, tsv, xls, xlsx and od' +
    's format.' +
    ''
)
KEYWORDS = [
    'excel',
    'python',
    'pyexcel',
]

INSTALL_REQUIRES = [
    'pyexcel>=0.2.3',
    'Click>=5.0',
]

EXTRAS_REQUIRE = {
}

CLASSIFIERS = [
    'Topic :: Office/Business',
    'Topic :: Utilities',
    'Topic :: Software Development :: Libraries',
    'Programming Language :: Python',
    'License :: OSI Approved :: BSD License',
    'Intended Audience :: Developers',
]


def read_files(*files):
    """Read files into setup"""
    text = ""
    for single_file in files:
        text = text + read(single_file) + "\n"
    return text


def read(afile):
    """Read a file into setup"""
    with open(afile, 'r') as opened_file:
        return opened_file.read()


if __name__ == '__main__':
    setup(
        name=NAME,
        author=AUTHOR,
        version=VERSION,
        author_email=EMAIL,
        description=DESCRIPTION,
        install_requires=INSTALL_REQUIRES,
        keywords=KEYWORDS,
        extras_require=EXTRAS_REQUIRE,
        packages=PACKAGES,
        include_package_data=True,
        long_description=read_files('README.rst', 'CHANGELOG.rst'),
        zip_safe=False,
        tests_require=['nose'],
        license=LICENSE,
        entry_points=ENTRY_POINTS,
        classifiers=CLASSIFIERS
    )
