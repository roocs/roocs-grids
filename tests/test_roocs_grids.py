import os
from glob import glob

import pytest

from roocs_grids import get_grid_file, grid_annotations, grid_dict, grids_dir


def test_get_grid_file():
    with pytest.raises(Exception, match="Unknown grid id: rubbish"):
        get_grid_file("rubbish")

    gf = get_grid_file("0pt25deg")
    assert os.path.isfile(gf)
    assert gf.endswith("roocs_grids/grids/cmip6_720x1440_scrip.20181001.nc")


@pytest.mark.parametrize(
    "grid_id,filename", [(key, grid_dict[key]) for key in grid_dict]
)
def test_grid_avail(grid_id, filename):
    with pytest.raises(Exception, match="Unknown grid id: rubbish"):
        get_grid_file("rubbish")

    gf = get_grid_file(grid_id)
    assert os.path.isfile(gf)
    assert gf.endswith(f"roocs_grids/grids/{filename}")
    assert grid_annotations[grid_id] != ""


def test_dict_completeness():
    """Test that grid_annotations and grid_dict include all available grids."""
    # Find all files in the grids directory
    grid_files = [os.path.basename(f) for f in glob(f"{grids_dir}/*")]

    # Make sure they exist in grid_dict
    # (test_grid_avail already tests that all grids have annotations)
    for f in grid_files:
        assert f in grid_dict.values()
