#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

DB_NAME='postgres'
CONTAINER_NAME='tarkir-db'
#POSTGRES_HOME='/var/lib/postgresql'
DUMP_PATH_CONTAINER="/tmp/dump-$(date +'%s%N').sql"
DUMP_PATH_HOST="${SCRIPT_DIR}/resources/dump-$(date +'%s%N').sql"

echo "Create and export new SQL-dump..."
docker-compose exec ${CONTAINER_NAME} bash -c \
  "su -c \"pg_dump --clean -Z 0 -d ${DB_NAME} \
  | sed -e '/^--/d' \
  | sed -e '/^$/d' \
  > ${DUMP_PATH_CONTAINER}\" postgres"

container_id=$(docker-compose ps -q ${CONTAINER_NAME})
docker cp "${container_id}":"${DUMP_PATH_CONTAINER}" "${DUMP_PATH_HOST}"

echo "Done and stored to ${DUMP_PATH_HOST}"
