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

def main(args):
    variable_name=args.variable_name
    url=args.url
    lon=args.lon
    lat=args.lat
    nearest_neighbors=args.kmax

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
    sys.exit(main(args))
