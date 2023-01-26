.PHONY: clean readme-toc tag

SHELL := /bin/bash
JOBS ?= 1

help:
	@echo "	clean"
	@echo "		Remove Python/build artifacts."
	@echo "	gen-pwd"
	@echo "		Add a user and pwd to the recognized users"
	@echo "	run"
	@echo "		Launch nginx and the server using docker-compose"

.ONESHELL:
gen-pwd:
	# e.g.: gen-pwd user=john pwd=123
	if [[ -f ./nginx/htpasswd ]]; then
		htpasswd -b nginx/htpasswd $$user $$pwd
	else
		htpasswd -c -b nginx/htpasswd $$user $$pwd
	fi

run:
	docker-compose up -d nginx

