# Florida Kayaking Map

![Sample Images](https://github.com/nth0007/Florida-Kayaking-Map/blob/master/images/combined_1000px.png)

This project started out of a desire to plot GPS tracks from kayaking trips around Florida over a medium resolution raster of the state. I had difficulty finding a georeferenced raster of high enough resolution, so I opted to make my own. The resulting images are mosaics assembled from fourteen Landsat 8 scenes.

## Images Available for Download

* [Florida 100m Resolution Natural Color geotif](https://drive.google.com/open?id=1Sg2E_HiEWjru_KhxURlG-DXYfCjEKSxE) - Bands 4, 3, and 2
* [Florida 100m Resolution False Color geotif](https://drive.google.com/open?id=14TWi1SzKqJdn5E-UXciueLCjRiw_I2MQ) - Bands 6, 5, and 4

## About Landsat Images

The mosaics available for download above were built from Landsat 8 imagery downloaded from the US Geological Survey's Earth Explorer website (see Tools section below). The website enables browsing of Landsat imagery and provides a variety of filters to make finding images as easy as possible. The images I used were found by searching Earth Explorer using a rough polygon outline of the state of Florida and filtering for "Level 1" (highest quality) images containing less than 10% cloud cover. It required a litle trial and error to find a minimal date range that covered the entire state of Florida and met the filter criteria. The "natural color" image uses Landsat 8 band numbers 4 (630–680 nm), 3 (525–600 nm), and 2 (450–515 nm) for RGB coloring, and the "false color" image uses band numbers 6 (1560–1660 nm), 5 (845–885 nm), and 4 (630–680 nm). The native resolution was 30 meters, but the mosaics are provided at 100 meter resolution.

## Included Files

The scripts below are used to create false and true color mosaics of Florida. The output images are available for download above.
* **process_imagery.py** - Run this to process the raw Landsat TIFs. This can be skipped if you download the mosaics included above.
* **tl_2016_12_cousub.shp** - US Census Bureau shape file (2016) used to crop the raw mosaic to the legal boundary of Florida.
* **untar_script.sh** - Unzips the raw Landsat download and removes unused bands.
* **scaleListTrue.csv** - Used to scale the brightness of each true color image to create a more seamless mosaic. The value specified in the right column is the desired 16-bit ceiling used when scaling to 8-bit.
* **scaleListFalse.csv** - Used to scale the brightness of each false color image to create a more seamless mosaic. The value specified in the right column is the desired 16-bit ceiling used when scaling to 8-bit.

The files below are used to combine GPX tracks and the Florida mosaics.
* **plot_tracks_over_map.py** - This plots GPX tracks over previously created mosaics.
* **track_list.txt** - A list of GPX tracks to include in the plot. Each line is the name of a .gpx file located in the same folder.

### Prerequisites

```
Linux
Python 3.7
rasterio 1.0.21
pyproj 1.9.6
gpx_parser 0.0.4
```

## Tools Used

* [USGS Earth Explorer](https://earthexplorer.usgs.gov/) - Free web source for browsing and downloading geoimages
* [GDAL](https://gdal.org/) - Library for manipulating geoimages
* [Rasterio](https://rasterio.readthedocs.io/en/stable/) - Python module used to read rasters
* [gpx_parser](https://github.com/kholkolg/gpx_parser/) - Python module used to parse GPX files

## Workflow
If building mosaics from raw Landsat imagery:
1. Download images (e.g. USGS Earth Explorer)
2. Run "untar_script.sh" to extract desired bands.
3. Run "process_imagery.py" to generate mosaics. This takes several minutes with a SSD.
4. Go kayaking/hiking/etc, record your trip with a GPS device, and export the track as a .gpx file.
5. Append the .gpx file name to "track_list.txt."
6. Run "plot_tracks_over_map.py" to combine GPX tracks with the mosaic.

If downloading mosaics from this page:
1. Download Florida_Boundary_100m_FalseColor.tif and/or Florida_Boundary_100m_TrueColor.tif from the links above
2. Go kayaking/hiking/etc, record your trip with a GPS device, and export the track as a .gpx file.
3. Append the .gpx file name to "track_list.txt."
4. Run "plot_tracks_over_map.py" to combine GPX tracks with the mosaic.
