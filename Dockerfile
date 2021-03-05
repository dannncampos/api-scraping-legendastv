FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# Bundle app source
COPY . /app

USER root

RUN apt-get update && apt-get install -y \
 python3 python3-pip

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip3 install -r requirements.txt
