COMMAND = python manage.py

run:
	$(COMMAND) runserver 0.0.0.0:3000

setup-dev:
	pip install -r requirements-dev.txt

migrations:
	$(COMMAND) makemigrations

migrate:
	$(COMMAND) migrate

check-migrations:
	$(COMMAND) check-migrations

test:
	$(COMMAND) test

test-nomigrations:
	$(COMMAND) test --nomigrations

lint:
	black --check .
	isort --check .

lint-fix:
	black .
	isort .

up:
	docker compose up -d --build

up-attached:
	docker compose up --build

down:
	docker compose down -v

clog-app: up
	docker compose logs app

ctest: up
	docker compose exec app $(COMMAND) test
	make down

ctest-nomigrations: up
	docker compose exec app $(COMMAND) test --nomigrations
	make down

clint: up
	docker compose exec app black --check .
	docker compose exec app isort --check .
	make down

clint-fix: up
	docker compose exec app black .
	docker compose exec app isort .
	make down
