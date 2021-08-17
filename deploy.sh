#!/bin/bash

if ! container-builder --help >> /dev/null ; then
    echo 'Install Docker Container Builer tool by following ' \
      https://github.com/fadich/docker-container-builder#install
    exit 1
fi;


TAG=${1:-latest}

docker login --username fadich95 \
  && container-builder build ./src tarkir-tools \
      --repository=fadich95/tarkir-tools \
      --tag=${TAG} \
      --push
