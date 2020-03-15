SHELL := /bin/bash
lint:
	@printf '\xf0\x9f\x94\x8d  \e[1;32mChecking code quality and style\e[0m\n'
	flake8 --ignore ./addons/ addons-dev/ */migrations/ .
	black --check .

format:
	@printf '\xf0\x9f\x96\xA4  \e[1;32mBlackening the code\e[0m\n'
	black .

test:
	@printf '\xf0\x9f\x94\x8d  \e[1;32mRunning tests\e[0m\n'
	docker-compose run web python manage.py test

run:
	@printf '\xf0\x9f\x94\x8d  \e[1;32mStarting Django Invoice\e[0m\n'
