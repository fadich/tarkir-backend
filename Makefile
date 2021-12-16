all: down build up

up:
	docker-compose -f ./src/docker-compose.yml up

down:
	docker-compose -f ./src/docker-compose.yml down

build:
	docker-compose -f ./src/docker-compose.yml build

db:
	docker-compose -f ./src/docker-compose.yml up tarkir-db

db-detach:
	docker-compose -f ./src/docker-compose.yml up -d tarkir-db

api:
	docker-compose -f ./src/docker-compose.yml up api

migration:
	docker-compose -f ./src/docker-compose.yml run --rm api flask db migrate -m "$(m)"
	sudo chown -R ${USER}:${USER} ./src/migrations/versions

data-migration:
	docker-compose -f ./src/docker-compose.yml run --rm api flask db revision -m "DM: $(m)"
	sudo chown -R ${USER}:${USER} ./src/migrations/versions

migrate:
	docker-compose -f ./src/docker-compose.yml run --rm api flask db upgrade

migrate-down:
	docker-compose -f ./src/docker-compose.yml run --rm api flask db downgrade

db-import:
	cd src/ && ../scripts/db-import.sh && cd ..

db-export:
	cd src/ && ../scripts/db-export.sh && cd ..

bash:
	docker-compose -f ./src/docker-compose.yml run --rm api bash
