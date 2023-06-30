.ONESHELL:
ENV_PREFIX=$(shell python -c "if __import__('pathlib').Path('.venv/bin/pip').exists(): print('.venv/bin/')")

.PHONY: help
help:  ## Show the help.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep

.PHONY: setup
setup:  ## Execute installation.
	@echo "Setting up project."
	@pip3 install --upgrade setuptools
	@echo "Installing testing dependencies."
	@pip3 install -r requirements-test.txt
	@echo "Setting up project requirements."
	@pip3 install -r requirements.txt
	@echo "Project setup complete!"
	
.PHONY: run
run:  ## Launch app.
	@echo "Running main app..."
	@python3 app.py live --camera 0 --style hot

.PHONY: test
test:  ## Run PyTest unit tests.
	@echo "Running unittest suite..."
	@pytest -vv -rA

.PHONY: lint
lint:  ## Run pep8, black, mypy linters.
	$(ENV_PREFIX)pylint torchcam/
	$(ENV_PREFIX)flake8 torchcam/
	$(ENV_PREFIX)black -l 80 --check torchcam/
	$(ENV_PREFIX)mypy --ignore-missing-imports torchcam/

.PHONY: show
show:  ## Show the current environment.
	@echo "Current environment:"
	@if [ "$(USING_POETRY)" ]; then poetry env info && exit; fi
	@echo "Running using $(ENV_PREFIX)"
	@$(ENV_PREFIX)python -V
	@$(ENV_PREFIX)python -m site

.PHONY: clean
clean:  ## Clean unused files.
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
	@rm -rf .venv
	@echo "Cleaned out unused files and directories!"

.PHONY: test-build
test-build: 
	@python3 -m venv .venv
	@source ./.venv/bin/activate
	@echo "Setting up project..."
	@pip3 install --upgrade setuptools
	@pip3 install -r requirements-test.txt
	@pip3 install -r requirements.txt
	@echo "Project build complete!"
	@pip install .