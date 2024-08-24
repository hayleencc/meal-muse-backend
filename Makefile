POETRY=poetry

install:
	$(POETRY) install

run:
	uvicorn main:app --reload --port 8000

override AUTOFLAKE_FORMAT=echo Run autoflake...; autoflake \
	--remove-all-unused-imports \
	--remove-unused-variables \
	--recursive \
	--in-place . \
	--exclude=__init__.py \
	--exclude=.venv/ \
	--exclude=data/;

format:
	${AUTOFLAKE_FORMAT}
	echo Run black...; black .;
	echo Run isort...; isort .;
	echo Run flake8...; flake8 .;

lint:
	$(POETRY) run flake8 
	$(POETRY) run black .
	$(POETRY) run isort .

test:
	export PYTHONPATH=$(pwd):$PYTHONPATH;
	poetry run coverage run -m pytest;
	poetry run coverage report;

test-ci:
    poetry run coverage run -m pytest
    poetry run coverage report
    poetry run coverage html

