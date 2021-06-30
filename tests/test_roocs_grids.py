import os
import pytest

from roocs_grids import get_grid_file


def test_get_grid_file():
    with pytest.raises(Exception, match="Unknown grid id: rubbish"): 
        get_grid_file("rubbish")

    gf = get_grid_file("0pt25deg")
    assert os.path.isfile(gf)
    assert gf.endswith("roocs_grids/grids/cmip6_720x1440_scrip.20181001.nc")

