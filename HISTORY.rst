Version History
===============

v0.1.2 (unreleased)
-------------------

Bug Fixes
^^^^^^^^^

* Added basic CI workflows
* Replaced setuptools with flit and pyproject.toml
* Added AUTHORS.rst and bump2version configuration
* Linting with ruff
* Made testing safer with non-POSIX environments


v0.1.1 (2023-10-20)
-------------------

Bug Fixes
^^^^^^^^^

* Added MANIFEST.in

v0.1.0 (2023-10-20)
-------------------

New Features
^^^^^^^^^^^^
* Added grid files in netCDF format:
 - World_Ocean_Atlas
 - MERRA-2
 - ERA-Interim
 - ERA-40
 - ERA5
 - Gaussian grids associated to spectral grid representations: T31, T42, T63, T127, T255
* Added tests to ensure completeness of grid descriptions.
* Added tests to ensure presence of grid files.
