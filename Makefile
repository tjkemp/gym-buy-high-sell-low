.PHONY: all
all: qa test

.PHONY: qa
qa:
	@pre-commit run --all-files

.PHONY: test
pytest:
	@pytest

.PHONY: coverage
coverage:
	@coverage report -m

.PHONY: security
security:
	@safety check
	@bandit --ini .bandit

.PHONY: update
update:
	@pip-compile --upgrade requirements/requirements.in
	@pip-sync requirements/requirements.txt

.PHONY: clean
clean:
	@coverage erase
	@py3clean .
	@rm -r .pytest_cache
