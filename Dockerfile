FROM ubuntu:14.04.4
MAINTAINER bitard [dot] michael [at] gmail [dot] com

RUN apt-get update && \
    apt-get install -y git wget unzip && \
    apt-get install -y python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose python-pip

RUN mkdir /root/.ssh/
ADD /home/lordlabakdas/.ssh/id_rsa /root/.ssh/id_rsa
RUN touch /root/.ssh/known_hosts
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

WORKDIR munchtron
EXPOSE 8100 8101

RUN git clone git@github.com:lordlabakdas/MunchTron.git munchtron
