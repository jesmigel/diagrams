FROM python:3.8-slim-buster AS builder

RUN apt update \
    && apt install --no-install-recommends -y \
    python-pydot python-pydot-ng graphviz \
    && apt autoremove -y \
    && rm -rf /var/lib/apt/lists/*

FROM builder as builder2
COPY --from=builder /usr/bin/ /usr/bin
ADD ./requirements /tmp/requirements
WORKDIR /tmp/requirements
RUN /usr/local/bin/python -m pip install --upgrade pip \
    && pip install -r pip3.txt
WORKDIR /tmp/proj