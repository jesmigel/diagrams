FROM python:3.8.2-buster

ADD ./requirements /tmp/requirements

WORKDIR /tmp/requirements

RUN apt update && apt install --no-install-recommends -y python-pydot python-pydot-ng graphviz && apt autoremove -y
RUN pip3 install -r pip3.txt

WORKDIR /tmp/proj