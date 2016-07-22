FROM ubuntu:14.04.4
MAINTAINER bitard [dot] michael [at] gmail [dot] com

RUN apt-get update && \
    apt-get install -y git wget unzip && \
    apt-get install -y python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose python-pip

WORKDIR MunchTron
EXPOSE 8100 8101
