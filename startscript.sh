docker start $1
docker exec -ti $1 script /dev/null -c 'bash -ilc tmux'
