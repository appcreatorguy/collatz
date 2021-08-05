.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

build: clean
	py setup.py bdist_wheel --universal

clean: clean-build clean-pyc ## Remove all build and python artifacts

clean-build: ## remove build artifacts
	rm -rf *.egg-info/
	rm -rf dist/
	rm -rf build/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -rf {} +
	find . -name '*.eggs' -exec rm -fr {} +

clean-pyc: ## remove Python file artifacts
	python -Bc "import pathlib; import shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__')]"

run:
	python -m simple_collatz

lint: ## check style with flake8, isort and black
	black simple_collatz
	isort simple_collatz
	flake8 simple_collatz

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist