FROM ubuntu:12.04

RUN sed -i "s/archive.ubuntu.com/ftp.daumkakao.com/g" /etc/apt/sources.list
RUN apt-get update
RUN apt-get -qq install default-jdk ant build-essential autoconf automake
RUN apt-get -qq install libtool libcppunit-dev python-setuptools python-dev git

RUN git clone https://github.com/naver/arcus.git
WORKDIR /arcus/scripts
RUN ./build.sh
ADD run.sh /arcus/run.sh

WORKDIR /arcus
RUN useradd arcus
RUN chown -R arcus:arcus .

USER arcus
EXPOSE 11211
