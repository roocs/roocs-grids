"""The setup script."""

__author__ = "Ag Stephens"
__contact__ = "ag.stephens@stfc.ac.uk"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__version__ = "0.1.1"

import os

from setuptools import find_packages, setup

# One strategy for storing the overall version is to put it in the top-level
# package's __init__ but Nb. __init__.py files are not needed to declare
# packages in Python 3

# Populate long description setting with content of README
#
# Use markdown format read me file as GitHub will render it automatically
# on package page
here = os.path.abspath(os.path.dirname(__file__))
#_long_description = open(os.path.join(here, "README.rst")).read()
_long_description = "roocs-grids: Grid definitions for the roocs regridder"

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
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description="Grid definitions for the roocs regridder",
    license_files=["LICENSE"],
    python_requires=">=3.8.0",
    install_requires=requirements,
    long_description=_long_description,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="roocs_grids, regrid, grid, interpolate, cmip",
    name="roocs_grids",
    packages=find_packages(include=["roocs_grids"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    package_data={"roocs_grids": ["grids/*"]},
    url="https://github.com/roocs/roocs-grids",
    version=__version__,
    zip_safe=False,
)
