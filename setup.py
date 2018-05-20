#!/usr/bin/env python3
import os
import sys
from setuptools import setup, find_packages
from dyson import __version__, __author__

sys.path.insert(0, os.path.abspath('lib'))
setup(
    name="dyson",
    description="Dyson Selenium framework.",
    version=__version__,
    author=__author__,
    author_email="sircapsalot@gmail.com",
    url="https://github.com/dyson-framework/dyson",
    download_url="https://github.com/dyson-framework/dyson/tarball/%s" % __version__,
    license="Apache 2",
    package_dir={'': 'lib'},
    packages=find_packages('lib'),
    install_requires=['PyYAML', 'jinja2', 'six', 'selenium'],
    classifiers=[],
    keywords=['selenium', 'testing'],
    scripts=[
        "bin/dyson",
        "bin/dyson-test",
        "bin/dyson-suite",
        "bin/dyson-sphere",
    ],
    data_files=[],
)
