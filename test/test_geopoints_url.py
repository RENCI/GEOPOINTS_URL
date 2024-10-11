"""
    Test geopoints_url - Tests geopoints url functionality

    Authors: Dr. Jeff Tilson, Phil Owen @RENCI.org
"""

import geopoints_url


def test_geopoints_url():
    """
        This tests the "geopoints url" functionality

    """

    # initialize the input arguments
    # --url "https://apsviz-thredds-dev.apps.renci.org/thredds/dodsC/2023/gfs/2023052300/wnat_53k_v1.0/sapelo2/adcirc_gfs_53k/gfsforecast/fort.63.nc" --variable_name 'zeta' --lon -79.6725155674 --lat 32.8596518752
    # --url 'http://tdsres.apps.renci.org/thredds/dodsC/datalayers/test/fort.63.nc' --variable_name 'zeta' --lon -79.6725155674 --lat 32.8596518752
    # --url 'http://tdsres.apps.renci.org/thredds/dodsC/datalayers/test/fort.63.d0.no-unlim.T.nc' --variable_name 'zeta' --lon -79.6725155674 --lat 32.8596518752
    # --url 'http://tdsres.apps.renci.org/thredds/dodsC/datalayers/test/fort.63.d0.no-unlim.T.rc.nc' --variable_name 'zeta' --lon -79.6725155674 --lat 32.8596518752

    # call the function, check the return
    ret_val = True

    # assert any errors
    assert ret_val
