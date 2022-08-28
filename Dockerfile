FROM python:3.7.8

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

ENV PATH_PROJECT=/home/docker/app

ENV PATH=/home/docker/.local/bin:$PATH

RUN useradd --create-home docker

# RUN chown docker:docker -R ${PATH_PROJECT}

# Install necessary system operational libs
# RUN apt-get update

USER docker

# Copy requirements
COPY requirements.txt requirements-dev.txt ${PATH_PROJECT}/

# Install pip requirements
RUN pip install --upgrade pip
RUN python -m pip install --ignore-installed -r ${PATH_PROJECT}/requirements-dev.txt

# Create app directory
WORKDIR ${PATH_PROJECT}
