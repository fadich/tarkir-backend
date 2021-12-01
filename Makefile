all: build up

up:
	docker-compose -f ./src/docker-compose.yml up

build:
	docker-compose -f ./src/docker-compose.yml build

migrations:
	docker-compose -f ./src/docker-compose.yml run --rm api flask db migrate -m "$(m)"
	sudo chown -R ${USER}:${USER} ./src/migrations/versions

migrate:
	docker-compose -f ./src/docker-compose.yml run --rm api flask db upgrade

migrate-down:
	docker-compose -f ./src/docker-compose.yml run --rm api flask db downgrade
