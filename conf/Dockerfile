FROM ubuntu:16.10

RUN apt-get update -y
RUN apt-get install -y build-essential 
RUN apt-get install -y wget
RUN apt-get install -y xz-utils
RUN apt-get install -y python
RUN apt-get install -y python-dev python-setuptools
ADD get-pip.py /get-pip.py
RUN python /get-pip.py
RUN apt-get install -y libcupti-dev
RUN pip install numpy
RUN pip install scipy
RUN pip install matplotlib
RUN pip install scikit-learn
RUN pip install tensorflow
#python zip
RUN mkdir /code
WORKDIR /code
