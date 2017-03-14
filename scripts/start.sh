docker start tensor-dev
docker exec -it \
	tensor-dev \
	/bin/bash -c "pip --version && python --version && /bin/bash"
