"""Grid definitions for the roocs regridder."""
import pathlib

__author__ = "Martin Schupfner"
__email__ = "schupfner@dkrz.de"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__version__ = "0.1.2"

pkg_dir = pathlib.Path(__file__).parent.absolute()

grid_dict = {
    "0pt25deg": "cmip6_720x1440_scrip.20181001.nc",
    "World_Ocean_Atlas": "cmip6_180x360_scrip.20181001.nc",
    "1deg": "cmip6_180x360_scrip.20181001.nc",
    "2pt5deg": "cmip6_72x144_scrip.20181001.nc",
    "MERRA-2": "cmip6_361x576_scrip.20181001.nc",
    "0pt625x0pt5deg": "cmip6_361x576_scrip.20181001.nc",
    "ERA-Interim": "cmip6_241x480_scrip.20181001.nc",
    "0pt75deg": "cmip6_241x480_scrip.20181001.nc",
    "ERA-40": "cmip6_145x288_scrip.20181001.nc",
    "1pt25deg": "cmip6_145x288_scrip.20181001.nc",
    "ERA5": "cmip6_721x1440_scrip.20181001.nc",
    "0pt25deg_era5": "cmip6_721x1440_scrip.20181001.nc",
    "0pt25deg_era5_lsm": "land_sea_mask_025degree_ERA5.nc",  # short lsm
    "0pt5deg_lsm": "land_sea_mask_05degree.nc4",  # float sftlf
    "1deg_lsm": "land_sea_mask_1degree.nc4",  # float sftlf
    "2deg_lsm": "land_sea_mask_2degree.nc4",  # float sftlf
    "0pt25deg_era5_lsm_binary": "land_sea_mask_025degree_binary.nc4",  # float sftlf cut at >= 0.5 land/sea
    "1deg_lsm_binary": "land_sea_mask_1degree_binary.nc4",  # float sftlf cut at >= 0.5 land/sea
    "2deg_lsm_binary": "land_sea_mask_2degree_binary.nc4",  # float sftlf cut at >= 0.5 land/sea
    "T31": "grid_T31.nc",
    "T42": "grid_T42.nc",
    "T63_lsm_binary": "grid_T63_lsm_binary.nc",  # float sftlf
    "T127_lsm_binary": "grid_T127_lsm_binary.nc",  # float sftlf
    "T255": "grid_T255.nc",
}

grid_annotations = {
    "0pt25deg": "Global 0.25 degree grid with one cell centered at 0.125E,0.125N ",
    "World_Ocean_Atlas": "Global 1.0 degree grid with one cell centered at 0.5E,0.5N."
    " As used by the World Ocean Atlas.",
    "1deg": "Global 1.0 degree grid with one cell centered at 0.5E,0.5N."
    " As used by the World Ocean Atlas.",
    "2pt5deg": "Global 2.5 degree grid with one cell centered at 1.25E,1.25N.",
    "MERRA-2": "Global 0.65x0.5 (latxlon) degree grid with one cell centered at 0E,0N."
    " As used by MERRA-2.",
    "0pt625x0pt5deg": "Global 0.65x0.5 (latxlon) degree grid with one cell centered at 0E,0N."
    " As used by MERRA-2.",
    "ERA-Interim": "Global 0.75 degree grid with one cell centered at 0E,0N."
    " As used by ERA-Interim.",
    "0pt75deg": "Global 0.75 degree grid with one cell centered at 0E,0N. As used by ERA-Interim.",
    "ERA-40": "Global 1.25 degree grid with one cell centered at 0E,0N. As used by ERA-40.",
    "1pt25deg": "Global 1.25 degree grid with one cell centered at 0E,0N. As used by ERA-40.",
    "ERA5": "Global 0.25 degree grid with one cell centered at 0E,0N. As used by ERA-5.",
    "0pt25deg_era5": "Global 0.25 degree grid with one cell centered at 0E,0N. As used by ERA-5.",
    "0pt25deg_era5_lsm": "Global 0.25 degree grid with one cell centered at 0E,0N."
    " As used by ERA-5. Includes a fractional land-sea mask.",
    "0pt5deg_lsm": "Global 0.5 degree grid with one cell centered at 0.25E,0.25N."
    " Includes a fractional land-sea mask.",
    "1deg_lsm": "Global 1.0 degree grid with one cell centered at 0.5E,0.5N."
    " As used by the World Ocean Atlas. Includes a fractional land-sea mask.",
    "2deg_lsm": "Global 2.0 degree grid with one cell centered at 1.0E,1.0N.",
    "0pt25deg_era5_lsm_binary": "Global 0.25 degree grid with one cell centered at 0E,0N."
    " As used by ERA-5. Includes a binary land-sea mask with"
    " land/sea fraction cut at >=0.5.",
    "1deg_lsm_binary": "Global 1.0 degree grid with one cell centered at 0.5E,0.5N."
    " As used by the World Ocean Atlas."
    " Includes a binary land-sea mask with land/sea fraction cut at >=0.5.",
    "2deg_lsm_binary": "Global 2.0 degree grid with one cell centered at 1.0E,1.0N."
    " Includes a binary land-sea mask with land/sea fraction cut at >=0.5. ",
    "T31": "Gaussian global grid of approx. 3.8 degree resolution,"
    " 48x96 nlatxnlon. Associated to a T31 spectral grid representation.",
    "T42": "Gaussian global grid of approx. 2.8 degree resolution,"
    " 64x128 nlatxnlon. Associated to a T42 spectral grid representation.",
    "T63_lsm_binary": "Gaussian global grid of approx. 1.9 degree resolution,"
    " 96x192 nlatxnlon. Associated to a T63 spectral grid representation. "
    " Includes a binary land-sea mask.",
    "T127_lsm_binary": "Gaussian global grid of approx. 1.0 degree resolution,"
    " 192x384 nlatxnlon. Associated to a T127 spectral grid representation."
    " Includes a binary land-sea mask.",
    "T255": "Gaussian global grid of approx. 0.5 degree resolution,"
    " 384x768 nlatxnlon. Associated to a T255 spectral grid representation.",
}

grids_dir = pathlib.Path(pkg_dir).joinpath("grids")


def get_grid_file(grid_id: str) -> pathlib.Path:
    if grid_id not in grid_dict:
        raise FileNotFoundError(f"Unknown grid id: {grid_id}")

    return pathlib.Path(grids_dir).joinpath(grid_dict[grid_id])
