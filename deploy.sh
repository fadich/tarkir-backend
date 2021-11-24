#!/bin/bash

if ! container-builder --help >> /dev/null ; then
    echo 'Install Docker Container Builder tool by following ' \
      https://github.com/fadich/docker-container-builder#install
    exit 1
fi;

# Default tag value is 'latest'
TAG='latest'

while [ $# -gt 0 ]; do
  case "$1" in
    --tag=*)
      TAG="${1#*=}"
      ;;
    --quiet)
      QUIET_ARGUMENT="--quiet"
      ;;
    --password=*)
      PASSWORD_ARGUMENT="--password=${1#*=}"
      ;;
    *)
      printf "* Error: Invalid argument %s.\n", "${1}"
      exit 1
  esac
  shift
done


docker login --username fadich95 "${PASSWORD_ARGUMENT}" \
  && container-builder build ./src tarkir-tools \
      --repository=fadich95/tarkir-tools \
      --tag=${TAG} \
      ${QUIET_ARGUMENT} \
      --push
