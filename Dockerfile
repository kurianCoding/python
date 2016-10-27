FROM ubuntu:16.10
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV TERM linux
ENV LC_ALL en_US.UTF-8  
RUN apt-get -y update
RUN apt-get install -y  curl nginx 
RUN apt-get install -y build-essential
RUN apt-get install -y zsh vim tmux
RUN apt-get install -y python-dev
ENV HOME /
ADD vimrc /.vimrc
ADD vim /.vim
ADD bashrc /.bashrc
CMD ["/bin/bash"]
