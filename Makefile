.PHONY: qa
qa:
	@pre-commit run --all-files
	@pytest
	# @bandit --ini .bandit

.PHONY: coverage
coverage:
	@coverage report -m

.PHONY: update-pip
update-pip:
	@python -m pip install --upgrade pip

.PHONY: update-deps
update-deps: update-pip
	@find requirements -name *.in -type f -exec sort -o {} {} \;
	@pip-compile --upgrade requirements/requirements.in
	@pip-sync requirements/requirements.txt
	@safety check

.PHONY: build
build: qa
	@python -m build

.PHONY: upload-test
upload-test: build
	@python -m twine upload --repository testpypi dist/*

.PHONY: release-prod
release-prod:
	@python -c "import gym_bhsl as bhsl; print('Check the version is correct: ', bhsl.__VERSION__, '- and tag it to create a release.')"
	@echo "git tag <tag_name> -m '<message>'"
	@echo "git push origin <tag_name>"

.PHONY: clean
clean:
	@coverage erase
	@py3clean .
	@rm -r .pytest_cache
	@rm -rf build
	@rm -rf dist
