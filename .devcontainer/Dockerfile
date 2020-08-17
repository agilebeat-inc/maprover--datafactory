FROM tensorflow/tensorflow:latest-gpu

LABEL maintainer Marek Dwulit<Marek.Dwulit@agilebeat.com>”

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get -y install vim mc git wget gcc g++
RUN apt-get -y install gnome-terminal --fix-missing

RUN pip install pylint pandas matplotlib rope importlib_resources autopep8
RUN /usr/bin/python3 -m pip install --upgrade pip