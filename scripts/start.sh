docker start python-dev
docker exec -it \
	python-dev \
	/bin/bash -c "pip --version && python --version && /bin/bash"
