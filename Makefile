.PHONY: install virtualenv ipython clean test

install:
		@echo "Installing for dev environment"
		@.venv/bin/python -m pip install -e '.[test,devel]'

virtualenv:
		@python -m venv .venv
		@source .venv/bin/activate

ipython:
		@.venv/bin/ipython

test:
		@.venv/bin/pytest -s -vv

watch:
		@.venv/bin/ptw -- -vv -s tests/

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