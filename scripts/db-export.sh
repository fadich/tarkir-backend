#!/usr/bin/env bash


if [ -z "${1}" ]
then
    DUMP_PATH_HOST="./dump-$(date +'%Y-%m-%d-%H-%M-%S').sql"
else
    DUMP_PATH_HOST="${1}"
fi

echo ${DUMP_PATH_HOST}

DB_NAME='postgres'
CONTAINER_NAME='tarkir-db'
DUMP_PATH_CONTAINER="/tmp/dump-$(date +'%Y-%m-%d-%H-%M-%S').sql"

echo "Create and export new SQL-dump..."
docker-compose exec ${CONTAINER_NAME} bash -c \
  "su -c \"pg_dump --clean -Z 0 -d ${DB_NAME} \
  | sed -e '/^--/d' \
  | sed -e '/^$/d' \
  > ${DUMP_PATH_CONTAINER}\" postgres"

echo "Extracting dump file from container..."
container_id=$(docker-compose ps -q ${CONTAINER_NAME})
docker cp "${container_id}":"${DUMP_PATH_CONTAINER}" "${DUMP_PATH_HOST}" || exit 1

echo "Done and stored to ${DUMP_PATH_HOST}"
