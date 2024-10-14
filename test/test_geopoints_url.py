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
    # get the URL of the TDS server
    tds_svr: str = os.getenv('TDS_SVR', None)

    # abort if no TDS server URL env param is declared
    assert tds_svr is not None

    # create a list of test urls
    urls: list = [
        # the test URL below is expected to point to the TDS-res in the prod namespace.
        # if running in k8s, the TDS service name can be used.
        tds_svr + "thredds/dodsC/2023/al4/16/NCSC_SAB_v1.23/ht-ncfs.renci.org/ncsc123_nhc_al042023/ofcl/fort.63.nc",
        ]

    # create a named tuple for the args to mimic the input
    argsNT = namedtuple('argsNT', ['lon', 'lat', 'variable_name', 'kmax', 'alt_urlsource', 'url',
                                   'keep_headers', 'ndays', 'ensemble'])

    # for each test url
    for url in urls:
        # init the named tuple for the call
        args = argsNT(-79.6725155674, 32.8596518752, 'zeta', 10, None, url, True, -4, None)

        # call the function, check the return
        ret_val = gu.main(args)

        # assert any errors
        assert ret_val is None
