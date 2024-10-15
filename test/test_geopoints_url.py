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
    tds_svr: str = os.getenv('TDS_SVR', 'https://apsviz-thredds-dev.apps.renci.org/')

    # abort if no TDS server URL env param is declared
    assert tds_svr is not None

    # open the file of test URLs
    try:
        # get the test data for now
        with open(os.path.join(os.path.dirname(__file__), 'url-list.txt'), 'r') as fh:
            # read in the whole file, split it into lines (URLs)
            urls = fh.read().splitlines()
    except FileNotFoundError:
        assert not 'File not found.'

    # create a named tuple for the args to mimic the cli input
    argsNT: namedtuple = namedtuple('argsNT', ['lon', 'lat', 'variable_name', 'kmax', 'alt_urlsource', 'url',
                                   'keep_headers', 'ensemble', 'ndays'])

    # for each test url
    for url in urls:
        # if the URL starts with <TDS_SVR> replace it with the tds_svr env parameter gathered above
        url = url.replace('<TDS_SVR>', tds_svr)

        # init the named tuple for the call
        args = argsNT(-79.6725155674, 32.8596518752, 'zeta', 10, None, url, True, None, 0)

        # call the function, check the return
        ret_val = gu.main(args)

        # assert any errors
        assert ret_val is None
