# Florida Kayaking Map

![Sample Images](https://github.com/nth0007/Florida-Kayaking-Map/blob/master/images/combined_1000px.png)

This project started out of a desire to plot GPS tracks from kayaking trips around Florida over a medium resolution raster of the state. I had difficulty finding a georeferenced raster of high enough resolution, so I opted to make my own. The resulting images are mosaics assembled from fourteen Landsat 8 scenes.

## Images Available for Download

* [Florida 100m Resolution Natural Color geotif](https://drive.google.com/open?id=1Sg2E_HiEWjru_KhxURlG-DXYfCjEKSxE) - Bands 4, 3, and 2
* [Florida 100m Resolution False Color geotif](https://drive.google.com/open?id=14TWi1SzKqJdn5E-UXciueLCjRiw_I2MQ) - Bands 6, 5, and 4

## About Landsat Images

The mosaics available for download above were built from Landsat 8 imagery downloaded from the US Geological Survey's Earth Explorer website (see Tools section below). The website enables browsing of Landsat imagery and provides a variety of filters to make finding images as easy as possible. The images I used were found by searching Earth Explorer using a rough polygon outline of the state of Florida and filtering for "Level 1" (highest quality) images containing less than 10% cloud cover. It required a litle trial and error to find a minimal date range that covered the entire state of Florida and met the filter criteria. The "natural color" image uses Landsat 8 band numbers 4 (630–680 nm), 3 (525–600 nm), and 2 (450–515 nm) for RGB coloring, and the "false color" image uses band numbers 6 (1560–1660 nm), 5 (845–885 nm), and 4 (630–680 nm). The native resolution was 30 meters, but the mosaics are provided at 100 meter resolution.

## Included Scripts

This project includes two scripts, "process_imagery.py" and "plot_tracks_over_map.py." The former uses system calls to various GDAL functions convert the raw Landsat rasters to a format useable by the latter.

### Prerequisites

```
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
