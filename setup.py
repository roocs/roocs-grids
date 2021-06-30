#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""

__author__ = "Ag Stephens"
__contact__ = "ag.stephens@stfc.ac.uk"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
__version__ = "0.1.0"

from setuptools import find_packages
from setuptools import setup
import os

# One strategy for storing the overall version is to put it in the top-level
# package's __init__ but Nb. __init__.py files are not needed to declare
# packages in Python 3

# Populate long description setting with content of README
#
# Use markdown format read me file as GitHub will render it automatically
# on package page
here = os.path.abspath(os.path.dirname(__file__))
_long_description = open(os.path.join(here, "README.rst")).read()

requirements = [line.strip() for line in open("requirements.txt")]

setup_requirements = [
    "pytest-runner",
]

test_requirements = ["pytest"]

setup(
    author=__author__,
    author_email=__contact__,
    # See:
    # https://www.python.org/dev/peps/pep-0301/#distutils-trove-classification
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Security",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering",
        "Topic :: System :: Distributed Computing",
        "Topic :: System :: Systems Administration :: Authentication/Directory",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description="Grid definitions for the roocs regridder",
    license=__license__,
    # This qualifier can be used to selectively exclude Python versions -
    # in this case early Python 2 and 3 releases
    python_requires=">=3.6.0",
    install_requires=requirements,
    long_description=_long_description,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="roocs_grids, regrid, grid, interpolate, cmip",
    name="roocs_grids",
    packages=find_packages(
        include=["roocs_grids"]
    ),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    package_data={"roocs_grids": ["grids/*"]},
    url="https://github.com/roocs/roocs-grids",
    version=__version__,
    zip_safe=False,
)
