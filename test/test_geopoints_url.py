"""
    Test geopoints_url - Tests geopoints url functionality

    Authors: Dr. Jeff Tilson, Phil Owen @RENCI.org
"""

import geopoints_url as gu
from collections import namedtuple


def test_geopoints_url():
    """
        This tests the "geopoints url" functionality

    """
    # example inputs

    # --url "https://apsviz-thredds-dev.apps.renci.org/thredds/dodsC/2023/gfs/2023052300/wnat_53k_v1.0/sapelo2/adcirc_gfs_53k/gfsforecast/fort.63.nc"
    # --variable_name 'zeta' --lon -79.6725155674 --lat 32.8596518752

    # --url 'https://tdsres.apps.renci.org/thredds/dodsC/Datalayers/test/fort.63.nc' --variable_name 'zeta' --lon -79.6725155674 --lat 32.8596518752

    # --url 'https://tdsres.apps.renci.org/thredds/dodsC/Datalayers/test/fort.63.d0.no-unlim.T.nc' --variable_name 'zeta' --lon -79.6725155674
    # --lat 32.8596518752

    # --url 'https://tdsres.apps.renci.org/thredds/dodsC/Datalayers/test/fort.63.d0.no-unlim.T.rc.nc' --variable_name 'zeta' --lon -79.6725155674
    # --lat 32.8596518752

    # create a list of test urls
    urls: list = [
        "https://apsviz-thredds-dev.apps.renci.org/thredds/dodsC/2023/gfs/2023052300/wnat_53k_v1.0/sapelo2/adcirc_gfs_53k/gfsforecast/fort.63.nc",
        # "https://tdsres.apps.renci.org/thredds/dodsC/Datalayers/test/fort.63.nc",
        # "https://tdsres.apps.renci.org/thredds/dodsC/Datalayers/test/fort.63.d0.no-unlim.T.nc",
        # "https://tdsres.apps.renci.org/thredds/dodsC/Datalayers/test/fort.63.d0.no-unlim.T.rc.nc"
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
