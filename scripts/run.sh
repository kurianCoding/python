docker rm -f tensor-dev
docker run --name=tensor-dev \
		-ti \
		-d \
		-h=tensor-dev \
		-v $PWD/../code:/code \
		$1 /bin/bash

