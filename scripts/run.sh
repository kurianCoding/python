docker rm -f python-dev
docker run --name=python-dev \
		-ti \
		-d \
		-h=python-dev \
		-v $PWD/../code:/code \
		$1 /bin/bash

