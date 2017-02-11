FROM ubuntu:16.10

RUN apt-get update -y
RUN apt-get install -y build-essential 
RUN apt-get install -y wget
RUN apt-get install -y xz-utils
RUN apt-get install -y python
RUN apt-get install -y python-dev python-setuptools
RUN apt-get install -y python-pip
RUN pip install numpy
RUN pip install scipy
RUN pip install matplotlib
#python zip
RUN mkdir /code
WORKDIR /code
