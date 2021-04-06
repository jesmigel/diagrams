.PHONY: build up down clean logs test

_COMPOSE=docker-compose

build:
	$(_COMPOSE) build

up-d:
	$(_COMPOSE) up -d

up:
	$(_COMPOSE) up

down:
	$(_COMPOSE) down -v

gen: down
	rm -f data/homelab.png
	$(_COMPOSE) up -d

logs:
	$(_COMPOSE) logs

status:
	$(_COMPOSE) ps

login:
	$(_COMPOSE) exec diagram bash

test: down build up login