.DEFAULT_GOAL := build

documentation:
	@echo "Running docs"
	./bin/mm2github.py ./README.mm -w
	./scripts/gencli.py
	pdoc -o docs/ ./freeplane_tools --force

install_local:
	pip3 install .

pkg: clean documentation
	@echo "Running PKG"
	python3 setup.py sdist
	twine check dist/*

upload:
	@echo "Running upload"
	twine upload --repository freeplane-tools dist/*

build: pkg upload
	@echo "Running ALL"

clean:
	rm -rfv docs/* dist/* *.egg-info
