FROM mcr.microsoft.com/devcontainers/python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEVELOPMENTENV=1

# Install updates
RUN \
    export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get -y upgrade \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install requirements
COPY requirements.txt .
RUN \
    python -m pip install --upgrade pip \
    && python -m pip install -r requirements.txt \
    && rm requirements.txt
