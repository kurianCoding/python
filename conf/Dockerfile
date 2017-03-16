FROM ubuntu:16.10

RUN apt-get update -y
RUN apt-get install -y build-essential 
RUN apt-get install -y wget
RUN apt-get install -y xz-utils
RUN apt-get install -y python
RUN apt-get install -y python-dev python-setuptools
ADD get-pip.py /get-pip.py
RUN python /get-pip.py
#python zip
RUN mkdir /code
WORKDIR /code
