.PHONY: build up down clean logs test

_COMPOSE=docker-compose

build:
	$(_COMPOSE) build

up:
	$(_COMPOSE) up -d

down:
	$(_COMPOSE) down

gen: down
	rm -f data/homelab.png
	$(_COMPOSE) up -d

logs:
	$(_COMPOSE) logs


test:
	open -a "/Applications/Google Chrome.app" 'http://google.com/'