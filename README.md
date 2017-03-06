# docker-flask-gdal

This repo is intended as a learning tool to give me exposure to:
 1. Docker
 2. Flask
 3. GDAL

Build the docker image with `docker build -t docker-flask-gdal .`.

Upon build the necessary libraries and landsat images will be downloaded to the docker image.

Run the docker image from within the docker-flask-gdal folder with `docker run -d=False -t -p 80:80 /bin/bash -c "cd app; python main.py"`.

Once running, the container is exposed to `0.0.0.0`. Access the implemented vegetation indexes using `0.0.0.0/?index=<index>`. For example, to calculate and download the NDVI of the landsat scene, use `0.0.0.0/?index=ndvi`.

Note: Each call to the Flask server will cause the vegetation index to be calculated on the entire landsat scene. This is highly inefficient and will be an area of focus for the future of this repo.

Note 2: The script gdal_calc.py is included in this repo because it has a `Calc` function that the installed gdal_calc.py does not.
