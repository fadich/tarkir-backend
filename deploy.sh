#!/bin/bash


TAG=${1:-latest}

docker login --username fadich95 \
  && container-builder build ./src tarkir-tools \
      --repository=fadich95/tarkir-tools \
      --tag=${TAG} \
      --push
