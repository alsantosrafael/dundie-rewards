.PHONY: install virtualenv ipython clean test pflake8 fmt lint watch, docs, docs-serve, build, publish

docs:
		@mkdocs build --clean


docs-serve:
		@mkdocs serve


install:
		@echo "Installing for dev environment"
		@.venv/bin/python -m pip install -e '.[test,devel]'

virtualenv:
		@python -m venv .venv
		@source .venv/bin/activate

lint:
		@.venv/bin/pflake8 dundie

fmt:
		@.venv/bin/isort --profile=black -m 3 dundie tests integration
		@.venv/bin/black dundie tests integration

ipython:
		@.venv/bin/ipython

test:
		@.venv/bin/pytest -s -vvv --forked

watch:
		@.venv/bin/ptw -- -vv -s --forked tests/

clean:
		@find ./ -name '*.pyc' -exec rm -f {} \;
		@find ./ -name '__pycache__' -exec rm -rf {} \;
		@find ./ -name 'Thumbs.db' -exec rm -f {} \;
		@find ./ -name '*~' -exec rm -f {} \;
		@rm -rf .cache
		@rm -rf .pytest_cache
		@rm -rf .mypy_cache
		@rm -rf build
		@rm -rf dist
		@rm -rf *.egg-info
		@rm -rf htmlcov
		@rm -rf .tox/
		@rm -rf docs/_build

build:
		@python setup.py sdist bdist_wheel

publish:
		@twine upload --repository testpypi dist/* 
