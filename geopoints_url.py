'''
MIT License

Copyright (c) 2022,2023,2024 Renaissance Computing Institute

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

## Codes substantially derived from the utilities.py code written by Brian O. Blanton, RENCI

#!/usr/bin/env python
# coding: utf-8

import sys
import pandas as pd
import numpy as np
import time as tm
import utilities as utilities
import generate_urls_from_times as genurls

# load the logger class
from logger import LoggingUtil

# get the log level and directory from the environment (or default).
log_level, log_path = LoggingUtil.prep_for_logging()

# create a logger
logger = LoggingUtil.init_logging("geopoints_url", level=log_level, line_format='medium', log_file_path=log_path)

def strip_ensemble_from_url(urls)->str:
    """
    We mandate that the URLs input to this fetcher are those used to access the TDS data. The "ensemble" information will be in position .split('/')[-2]
    eg. 'http://tds.renci.org/thredds/dodsC/2021/nam/2021052318/hsofs/hatteras.renci.org/hsofs-nam-bob-2021/nowcast/fort.63.nc'
    
    Parameters:
        urls: list(str). list of valid urls
    Returns:
        Ensemble: <str>
    """
    url = grab_first_url_from_urllist(urls)
    try:
        words = url.split('/')
        ensemble=words[-2] # Usually nowcast,forecast, etc 
    except IndexError as e:
        print(f'strip_ensemble_from_url Uexpected failure try next:{e}')
    return ensemble

def first_true(iterable, default=False, pred=None):
    """
    itertools recipe found in the Python 3 docs
    Returns the first true value in the iterable.
    If no true value is found, returns *default*
    If *pred* is not None, returns the first item
    for which pred(item) is true.

    first_true([a,b,c], x) --> a or b or c or x
    first_true([a,b], x, f) --> a if f(a) else b if f(b) else x

    """
    return next(filter(pred, iterable), default)

def grab_first_url_from_urllist(urls)->str:
    """
    eg. 'http://tds.renci.org/thredds/dodsC/2021/nam/2021052318/hsofs/hatteras.renci.org/hsofs-nam-bob-2021/nowcast/fort.63.nc'
    
    Parameters:
        urls: list(str). list of valid urls
    Returns:
        url: <str> . Fetch first available, valid url in the list
    """
    if not isinstance(urls, list):
        print('first url: URLs must be in list form')
        sys.exit(1)
    url = first_true(urls)
    return url

def main(args):
    variable_name=args.variable_name
    url=args.url
    lon=args.lon
    lat=args.lat
    nearest_neighbors=args.kmax
    nhours=-24 # Look back 24 hours

    #print(f' Build list of URLs to fetch: nhours lookback is {nhours}')
    #rpl = genurls.generate_urls_from_times(url=url,timein=None, timeout=None, ndays=nhours, grid_name=None, instance_name=None, config_name=None)
    #new_urls = rpl.build_url_list_from_template_url_and_offset(ensemble=args.ensemble)
    #print(f' New URL list {new_urls}')

    print(f'Lon {lon}. Lat {lat}')
    print(f'Selected nearest neighbors values is {nearest_neighbors}')

    t0=tm.time()
    df_product_data, df_product_metadata, df_excluded = utilities.Combined_pipeline(url, variable_name, lon, lat, nearest_neighbors)
    df_product_data.to_csv(f'Product_data.csv',header=args.keep_headers)
    df_product_metadata.to_csv(f'Product_meta.csv',header=args.keep_headers)
    print(df_excluded)
    df_excluded.to_csv(f'Product_excluded_geopoints.csv')
    print(df_product_data)
    df_product_data.to_pickle(f'Product_data.pkl')
    print(f'Finished. Runtime was {tm.time()-t0}')

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--lon', action='store', dest='lon', default=None, type=float,
                        help='lon: longitiude value for time series extraction')
    parser.add_argument('--lat', action='store', dest='lat', default=None, type=float,
                        help='lat: latitude value for time series extraction')
    parser.add_argument('--variable_name', action='store', dest='variable_name', default='zeta', type=str,
                        help='Variable name of interest from the supplied url')
    parser.add_argument('--kmax', action='store', dest='kmax', default=10, type=int,
                        help='nearest_neighbors values when performing the Query')
    parser.add_argument('--alt_urlsource', action='store', dest='alt_urlsource', default=None, type=str,
                        help='Alternative location for the ADCIRC data - NOTE specific formatting requirements exist')
    parser.add_argument('--url', action='store', dest='url', default=None, type=str,
                        help='Specify FQ URL')
    parser.add_argument('--keep_headers', action='store_true', default=True,
                        help='Boolean: Indicates to add header names to output files')
    args = parser.parse_args()

    # log the input args
    logger.debug('input args: %s', args)

    sys.exit(main(args))
