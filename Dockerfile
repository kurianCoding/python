FROM ubuntu:16.10

RUN apt-get update -y
RUN apt-get install -y build-essential
RUN apt-get install -y wget
RUN apt-get install -y xz-utils
# ensure local python is preferred over distribution pythov
ENV PATH /usr/local/bin:$PATH

# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8
RUN apt-get update && apt-get install -y --no-install-recommends \
	    tcl \
	    tk \
	    && rm -rf /var/lib/apt/lists/*
ENV GPG_KEY C01E1CAD5EA2C4F0B8E3571504C367C218ADD4FF
ENV PYTHON_VERSION 2.7.13

RUN wget -O python.tar.xz "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
RUN mkdir -p /usr/src/python
RUN tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz 
RUN cd /usr/src/python \
	&& ./configure 
RUN cd /usr/src/python \
	&& make -j$(nproc) 
RUN cd /usr/src/python \
	&& make install 
RUN mkdir /code
WORKDIR /code
