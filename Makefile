# Установка и публикация
install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
# локально установлен python3.11
	python3.11 -m pip install --user dist/*.whl


# Запуск пакета brain-games
brain-games:
	poetry run brain-games