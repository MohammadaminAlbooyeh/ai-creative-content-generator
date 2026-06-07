.PHONY: install run test clean docker-up docker-down

install:
	pip install -r requirements.txt

run:
	uvicorn backend.main:app --reload

test:
	pytest tests/

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

migrate:
	alembic upgrade head

seed:
	python scripts/seed_data.py
