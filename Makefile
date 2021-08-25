.DEFAULT_GOAL := build

documentation:
	@echo "Running docs"
	bin/mm2bitbucket_server.py ./README.mm -w

install_local:
	pip3 install .

build: documentation
	@echo "Running build"
	python3 setup.py sdist
	twine upload --repository freeplane-tools dist/*

clean:
	rm -rfv dist/* *.egg-info
