docker rm -f mlDev
docker run --name=mlDev \
	-v $PWD/code:/code \
	-ti \
	$1 /bin/bash
