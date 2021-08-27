.DEFAULT_GOAL := pkg

docs := ./docs
srcdir := ./src
pkgname := freeplane_tools

documentation: clean
	@echo "Running docs"
	./bin/mm2github.py ./README.mm -w
	./scripts/gencli.py
	./scripts/genbadges.py
	./scripts/genpypyreadme.py
	pdoc -o $(docs) $(srcdir)/$(pkgname) --force --html
	mv $(docs)/$(pkgname)/* $(docs)/

docker_test:
	./scripts/dockertest.sh

install_local:
	pip3 install .

pkg: documentation docker_test
	@echo "Running PKG"
	python3 setup.py sdist
	twine check dist/*

upload:
	@echo "Running upload"
	twine upload --repository freeplane-tools dist/*

bump_version:
	# order is important here
	./scripts/version_bump.py
	./scripts/genchangelog.py
	git add ./CHANGELOG.md
	git add ./VERSION
	git diff HEAD
	git commit -S --amend
	bash -c "git tag v$$(cat VERSION)"

push:
	$(eval tag = $(shell cat VERSION))
	git push -u origin HEAD
	git push -u origin v$(tag)

release: pkg upload push
	@echo "Running Release"

clean:
	rm -rfv docs/* dist/* src/*.egg-info
