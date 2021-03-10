#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

DB_NAME='postgres'
CONTAINER_NAME='tarkir-db'
#POSTGRES_HOME='/var/lib/postgresql'
DUMP_PATH_CONTAINER="/tmp/dump-$(date +'%s%N').sql"
DUMP_PATH_HOST="${SCRIPT_DIR}/resources/dump.sql"

echo "Import SQL-dump..."
container_id=$(docker-compose ps -q ${CONTAINER_NAME})
docker cp "${DUMP_PATH_HOST}" "${container_id}":"${DUMP_PATH_CONTAINER}"

docker-compose exec ${CONTAINER_NAME} bash -c \
  "psql -U postgres -d ${DB_NAME} < ${DUMP_PATH_CONTAINER}"

echo "Done"
