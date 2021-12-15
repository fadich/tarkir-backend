#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

DB_NAME='postgres'
CONTAINER_NAME='tarkir-db'
#POSTGRES_HOME='/var/lib/postgresql'
DUMP_PATH_CONTAINER="/tmp/dump-$(date +'%Y-%m-%d-%H-%M-%S').sql"
if [ -z "${1}" ]
  then
    DUMP_PATH_HOST="${SCRIPT_DIR}/resources/dump.sql"
    echo "Getting default DB: ${DUMP_PATH_HOST}"
else
    DUMP_PATH_HOST="${1}"
fi

echo "Import SQL-dump..."
container_id=$(docker-compose ps -q ${CONTAINER_NAME})
docker cp "${DUMP_PATH_HOST}" "${container_id}":"${DUMP_PATH_CONTAINER}"

UPDATE_AUTOINCREMENTS_QUERY=$(cat <<-END
SELECT SETVAL('application_id_seq', (SELECT MAX(id) FROM application));
SELECT SETVAL('color_id_seq', (SELECT MAX(id) FROM color));
SELECT SETVAL('config_id_seq', (SELECT MAX(id) FROM config));
SELECT SETVAL('passive_bonus_id_seq', (SELECT MAX(id) FROM passive_bonus));
SELECT SETVAL('school_id_seq', (SELECT MAX(id) FROM school));
SELECT SETVAL('spell_id_seq', (SELECT MAX(id) FROM spell));
SELECT SETVAL('user_id_seq', (SELECT MAX(id) FROM user));
END
)


docker-compose exec ${CONTAINER_NAME} bash -c \
  "psql -U postgres -d ${DB_NAME} < ${DUMP_PATH_CONTAINER}"

docker-compose exec ${CONTAINER_NAME} bash -c \
  "psql -U postgres -d ${DB_NAME} -c \"${UPDATE_AUTOINCREMENTS_QUERY}\""

echo "Done"
