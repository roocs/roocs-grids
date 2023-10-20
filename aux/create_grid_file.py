from os.path import basename
from pathlib import Path

import xarray as xr
from clisops import core as clore

from roocs_grids import grids_dir, pkg_dir

#####################################################

# Specify the netcdf source file
source_file = "example.nc"

# Output filename
target_file = "grid_example.nc"

# Specify the global attributes
attr_dict = {
    "nominal_resolution": "x km",
    "grid": "Label, mxn longitude/latitude",
    "Conventions": "CF-1.7",
}


#####################################################


# Open xarray.Dataset
ds = xr.open_dataset(source_file)
# Create clore.Grid object
g = clore.Grid(ds)
# Drop variables and global attributes
# FIXME: This is broken in newer versions of xarray
g._drop_vars(keep_attrs=False)
# Add specified global attributes
g.ds.attrs.update(attr_dict)
# Save to disk
g.to_netcdf(filename=basename(target_file), folder=grids_dir)

print(f"Stored grid in '{Path(grids_dir, basename(target_file))}'.")
print(
    f"Please add a respective entry to grid_dict and grid_annotations in '{Path(pkg_dir, '__init__.py')}'."
)
