.PHONY: checklint checkmypy checkformat check test build installdev install publishdev publish clean

checklint:
	ruff check src/cdshelper src/tests

checkmypy:
	mypy src/cdshelper src/tests

checkformat:
	ruff format src/cdshelper src/tests

check: checklint checkmypy checkformat

ready: check test

test:
	pytest src/tests

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
