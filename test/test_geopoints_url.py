"""
    Test geopoints_url - Tests geopoints url functionality

    Authors: Jeffrey L. Tilson, Phil Owen @RENCI.org
"""

import os
import geopoints_url as gu
from collections import namedtuple


def test_geopoints_url():
    """
        This tests the "geopoints url" functionality

    """
    # example inputs

    # --url "<TDS_SVR>thredds/dodsC/2023/gfs/2023052300/wnat_53k_v1.0/sapelo2/adcirc_gfs_53k/gfsforecast/fort.63.nc"
    # --variable_name 'zeta' --lon -79.6725155674 --lat 32.8596518752

    # --url '<TDS_SVR>thredds/dodsC/Datalayers/test/fort.63.nc' --variable_name 'zeta' --lon -79.6725155674 --lat 32.8596518752

    # --url '<TDS_SVR>thredds/dodsC/Datalayers/test/fort.63.d0.no-unlim.T.nc' --variable_name 'zeta' --lon -79.6725155674
    # --lat 32.8596518752

    # --url '<TDS_SVR>thredds/dodsC/Datalayers/test/fort.63.d0.no-unlim.T.rc.nc' --variable_name 'zeta' --lon -79.6725155674
    # --lat 32.8596518752

    # get the URL of the TDS server
    tds_svr: str = os.getenv('TDS_SVR', None)

    # abort if no TDS server URL env param is declared
    assert tds_svr is not None

    # create a list of test urls
    urls: list = [
        tds_svr + "thredds/dodsC/2023/gfs/2023052300/wnat_53k_v1.0/sapelo2/adcirc_gfs_53k/gfsforecast/fort.63.nc",
        # tds_svr + "thredds/dodsC/Datalayers/test/fort.63.nc",
        # tds_svr + "thredds/dodsC/Datalayers/test/fort.63.d0.no-unlim.T.nc",
        # tds_svr + "thredds/dodsC/Datalayers/test/fort.63.d0.no-unlim.T.rc.nc"
        ]

    # create a named tuple for the args to mimic the input
    argsNT = namedtuple('argsNT', ['lon', 'lat', 'variable_name', 'kmax', 'alt_urlsource', 'url',  'keep_headers'])

    # for each test url
    for url in urls:
        # init the named tuple for the call
        args = argsNT(-79.6725155674, 32.8596518752, 'zeta', 10, None, url, True)

        # call the function, check the return
        ret_val = gu.main(args)

        # assert any errors
        assert ret_val is None
