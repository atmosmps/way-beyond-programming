COMMAND = python manage.py

local-server:
	manage.py runserver 0.0.0.0:8000

local-setup:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

migrations:
	$(COMMAND) makemigrations

migrate:
	$(COMMAND) migrate

check-migrations:
	$(COMMAND) check-migrations

test:
	$(COMMAND) test
