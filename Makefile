COMMAND = python manage.py

local-server:
	$(COMMAND) runserver 0.0.0.0:3000

local-setup:
	pip install -r requirements-dev.txt

local-migrations:
	$(COMMAND) makemigrations

local-migrate:
	$(COMMAND) migrate

local-check-migrations:
	$(COMMAND) check-migrations

local-test:
	$(COMMAND) test

local-test-nomigrations:
	$(COMMAND) test --nomigrations

local-lint:
	black --check .
	isort --check .

local-lint-fix:
	black .
	isort .

docker-server:
	docker-compose up -d --build

docker-server-attached:
	docker-compose up --build

docker-down:
	docker-compose down -v

docker-log-app: docker-server
	docker-compose logs app

docker-test: docker-server
	docker-compose exec app $(COMMAND) test
	make docker-down

docker-test-nomigrations: docker-server
	docker-compose exec app $(COMMAND) test --nomigrations
	make docker-down

docker-lint: docker-server
	docker-compose exec app black --check .
	docker-compose exec app isort --check .
	make docker-down

docker-lint-fix: docker-server
	docker-compose exec app black .
	docker-compose exec app isort .
	make docker-down
