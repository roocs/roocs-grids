import os

pkg_dir = os.path.dirname(__file__)


grid_dict = {
    "0pt25deg": "cmip6_720x1440_scrip.20181001.nc",  # one cell center @ 0.125E,0.125N
    "World_Ocean_Atlas": "cmip6_180x360_scrip.20181001.nc",  # one cell center @ 0.5E,0.5N
    "1deg": "cmip6_180x360_scrip.20181001.nc",  # one cell center @ 0.5E,0.5N
    "2pt5deg": "cmip6_72x144_scrip.20181001.nc",
    "MERRA-2": "cmip6_361x576_scrip.20181001.nc",
    "0pt625x0pt5deg": "cmip6_361x576_scrip.20181001.nc",
    "ERA-Interim": "cmip6_241x480_scrip.20181001.nc",
    "0pt75deg": "cmip6_241x480_scrip.20181001.nc",
    "ERA-40": "cmip6_145x288_scrip.20181001.nc",
    "1pt25deg": "cmip6_145x288_scrip.20181001.nc",
    "ERA5": "cmip6_721x1440_scrip.20181001.nc",
    "0pt25deg_era5": "cmip6_721x1440_scrip.20181001.nc",
    "0pt25deg_era5_lsm": "land_sea_mask_025degree_ERA5.nc",
    "0pt5deg_lsm": "land_sea_mask_05degree.nc4",
    "1deg_lsm": "land_sea_mask_1degree.nc4",
    "2deg_lsm": "land_sea_mask_2degree.nc4",
}

grids_dir = os.path.join(pkg_dir, "grids")


def get_grid_file(grid_id):
    if grid_id not in grid_dict:
        raise Exception(f"Unknown grid id: {grid_id}")

    return os.path.join(grids_dir, grid_dict[grid_id])


