FROM ubuntu:16.10

RUN apt-get update -y
RUN apt-get install -y build-essential
RUN apt-get install -y python-dev 
ADD ./get-pip.py /get-pip.py
RUN python /get-pip.py
RUN pip install scipy
RUN pip install numpy
RUN pip install scipy
RUN pip install scikit-learn
