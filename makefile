.PHONY: checklint checkmypy check build installdev install publishdev publish clean

checklint:
	ruff check src/cdshelper

checkmypy:
	mypy src/cdshelper

check: checklint checkmypy

build:
	python -m build . --sdist --wheel

installdev:
	python -m pip install --upgrade pip && pip install -e .[dev,test,mypy] --no-cache

install:
	python -m pip install --upgrade pip && pip install . --no-cache

publishdev:
	twine upload --verbose --repository testpypi dist/*

publish:
	twine upload --verbose --repository pypi dist/*

clean:
	rm -rf build dist
