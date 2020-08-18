install:
	poetry install

lint:
	poetry run flake8 brain_games

.PHONY: brain_games
