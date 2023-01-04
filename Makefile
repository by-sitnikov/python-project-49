# Установка и публикация
install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3.11 -m pip install --user dist/*.whl


# Запуск игры
brain-games:
	poetry run brain-games
brain-even:
	poetry run brain-even
brain-calc:
	poetry run brain-calc


# Линтер
lint:
	poetry run flake8 brain_games