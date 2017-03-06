import gdal_calc as raster_math

from collections import OrderedDict

image_files = OrderedDict([
    ("blue", "/app/data/B.TIF"),
    ("green", "/app/data/G.TIF"),
    ("red", "/app/data/R.TIF"),
    ("nir", "/app/data/NIR.TIF")
])


def vari():
    """Visible Atmospherically Resistant Index (VARI)

    http://www.harrisgeospatial.com/docs/BroadbandGreenness.html#Visible

    VARI = (G - R) / (G + R - B)
    """
    outfile = "/app/data/vari.tif"

    raster_math.Calc("(G - R) / (G + R - B)", G=image_files["green"],
         R=image_files["red"], B=image_files["blue"],
         outfile=outfile)

    return outfile

def ndvi():
    """Normalized Difference Vegetation Index (NDVI)

    http://www.harrisgeospatial.com/docs/BroadbandGreenness.html#NDVI

    NDVI = (NIR - R) / (NIR + R)
    """
    outfile = "/app/data/ndvi.tif"

    raster_math.Calc("(N - R) / (N + R)", N=image_files["nir"],
         R=image_files["red"], outfile=outfile)

    return outfile

def rdvi():
    """Renormalized Difference Vegetation Index (RDVI)

    http://www.harrisgeospatial.com/docs/BroadbandGreenness.html#Renormal

    NDVI = (NIR - R) / sqrt(NIR + R)
    """
    outfile = "/app/data/rdvi.tif"

    raster_math.Calc("(N - R) / sqrt(N + R)", N=image_files["nir"],
         R=image_files["red"], outfile=outfile)

    return outfile
