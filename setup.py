#!/usr/bin/env python3

from setuptools import setup, find_packages
from dyson import __version__, __author__

setup(
      name="Dyson",
      description="Dyson Selenium framework.",
      version=__version__,
      author=__author__,
      author_email="sircapsalot@gmail.com",
      url="http://dyson-framework.com",
      license="Apache 2",
      package_dir={'': 'lib'},
      packages=find_packages('lib'),
      install_requires=['PyYAML', 'jinja2', 'six', 'selenium'],
      classifiers=[],
      scripts=[
            "bin/dyson",
            "bin/dyson-test",
            "bin/dyson-suite",
            "bin/dyson-sphere",
      ],
      data_files=[],
)
