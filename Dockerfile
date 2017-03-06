FROM debian:jessie

COPY ./app /app

RUN apt-get -y update &&  \
	apt-get -y install python-pip python-gdal wget && \
	pip install flask # && \
	wget -O /data/B.TIF https://s3-us-west-2.amazonaws.com/landsat-pds/L8/026/031/LC80260312016165LGN00/LC80260312016165LGN00_B2.TIF && \
	wget -O /data/G.TIF https://s3-us-west-2.amazonaws.com/landsat-pds/L8/026/031/LC80260312016165LGN00/LC80260312016165LGN00_B3.TIF && \
	wget -O /data/NIR.TIF https://s3-us-west-2.amazonaws.com/landsat-pds/L8/026/031/LC80260312016165LGN00/LC80260312016165LGN00_B4.TIF && \
	wget -O /data/R.TIF https://s3-us-west-2.amazonaws.com/landsat-pds/L8/026/031/LC80260312016165LGN00/LC80260312016165LGN00_B5.TIF


# To build:
# docker build -t docker-flask-gdal .

# To run with app code mounted as volume:
# docker run -d=False -t -p 80:80 -v $(pwd)/docker-flask/app:/app docker-flask-gdal /bin/bash -c "cd app; python main.py"