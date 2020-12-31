#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:50:16 2019
"""
import numpy as np
import matplotlib.pyplot as plt
import pyproj
import rasterio
import gpx_parser as parser

# Options
for_print  = True  # Draw thicker lines for easier viewing at print resolutions
true_color = False # Use true color or false color imagery

# Point to source imagery
src_root         = './imagery/landsat8_set_2/'            # Update as needed
true_color_file  = 'Florida_Boundary_100m_TrueColor.tif'  # Download from Drive
false_color_file = 'Florida_Boundary_100m_FalseColor.tif' # Download from Drive

if true_color:
    src_path = src_root + true_color_file
    file_name_out = 'all_Florida_locations_TrueColor.png'
else:
    src_path = src_root + false_color_file
    file_name_out = 'all_Florida_locations_FalseColor.png'

if for_print:
    file_name_out = file_name_out.replace('.png', '_Print.png')
else:
    file_name_out = file_name_out.replace('.png', '_Fine.png')

src = rasterio.open(src_path)

# Get bands (out of 1, 2, 3)
r = src.read(1)
g = src.read(2)
b = src.read(3)

# Stack bands
rgb = np.dstack((r, g, b))

# Use pyproj to convert point coordinates
utm     = pyproj.Proj(src.crs) # Pass CRS of image from rasterio
lon_lat = pyproj.Proj(init='epsg:4326')

# Get image boundary
img_bound = (src.bounds.bottom, src.bounds.top, src.bounds.left, src.bounds.right)

# View the color composite
dpi = 1200

if for_print:
    linewidth = 0.35
else:
    linewidth = 0.075
    
plt.figure()
plt.imshow(rgb)

track_list = []
distList   = []
dur_list   = []
# Single column file containing list of track files
track_list_file = './tracks/track_list.txt'
with open(track_list_file) as fp:
   for cnt, line in enumerate(fp):
       track_list.append(line.strip(' \r\n'))

# GPX files are assumed to contain only one track segment - only reading first
for gpx_file_name in track_list:
    gpx_path = './tracks/' + gpx_file_name
    with open(gpx_path, 'r') as gpx_file:
        gpx = parser.parse(gpx_file)
        distM = gpx.length_2d()
        distList.append(distM)
        
        time_bounds = gpx.get_time_bounds()
        dur = time_bounds[-1] - time_bounds[0]
        dur_list.append(dur)
    
    # Test whether track is inside image boundary and exclude if not
    track_bound = gpx.get_bounds()
    top    = img_bound[0] < track_bound[0] < img_bound[1]
    bottom = img_bound[0] < track_bound[1] < img_bound[1]
    left   = img_bound[2] < track_bound[2] < img_bound[3]
    right  = img_bound[2] < track_bound[3] < img_bound[3]
    if top and bottom and left and right:
        show_track = True
    else:
        show_track = False
        print('Track', gpx_file_name, 'outside image boundary')
    
    if show_track:
        row_list = []
        col_list = []
        for point in gpx.tracks[0][0]:
            lat = point.latitude
            lon = point.longitude            
            east, north = pyproj.transform(lon_lat, utm, lon, lat)
            row, col = src.index(east, north) # spatial --> image coordinates
            row_list.append(row)
            col_list.append(col)
            
        plt.plot(col_list, row_list, 'r-', linewidth=linewidth)

tot_dist_meters = np.sum(distList)
tot_dist_miles = tot_dist_meters * 0.000621371
print('\nTotal distance:', np.round(tot_dist_miles, 1), 'miles')

total_dur = np.sum(dur_list)
max_dur   = np.max(dur_list)
avg_dur   = np.mean(dur_list)
print('Total duration:', total_dur)
print('Max duration:',   max_dur)
print('Avg duration:',   avg_dur)

# Draw and save image. Due to high resolution, this can take several seconds.
plt.axis('off')
plt.tight_layout()

plt.savefig(file_name_out, dpi=dpi, facecolor='black', edgecolor='black',
        bbox_inches='tight', frameon=None)

plt.show()