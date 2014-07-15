#!/usr/bin/env python3
"""data-plots: A collection of scripts for making various kinds of plots.

data-plots is a collection of scripts for making various scientific plots.
"""

DOCLINES = __doc__.split("\n")

CLASSIFIERS = """\
Programming Language :: Python
Programming Language :: Python :: 3
Intended Audience :: Science/Research
License :: OSI Approved :: MIT License
Operating System :: OS Independent
"""

MAJOR      = 0
MINOR      = 1
MICRO      = 0
ISRELEASED = False
PRERELEASE = 1
VERSION    = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

def get_version_info():
    FULLVERSION = VERSION

    if not ISRELEASED:
        FULLVERSION += '-pre' + str(PRERELEASE)

    return FULLVERSION

def setup_package():
    metadata = dict(
        name = 'data_plots',
        url = 'https://github.com/astroswego/data-plots',
        description = DOCLINES[0],
        long_description = "\n".join(DOCLINES[2:]),
        version = get_version_info(),
        package_dir = {'': 'src'},
        packages = [
            'data_plots',
            'data_plots_scripts'
        ],
        entry_points = {
            'console_scripts': [
                'data-plots = data_plots_scripts.data_plots:main'
            ]
        },
        keywords = [
            'plotting',
            'statistics'
        ],
        classifiers = [f for f in CLASSIFIERS.split('\n') if f],
        requires = [
            'numpy (>= 1.8.0)',
            'matplotlib (>= 1.3.0)'
        ]
    )

    from setuptools import setup

    setup(**metadata)

if __name__ == '__main__':
    setup_package()
