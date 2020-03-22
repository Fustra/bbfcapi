MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

COLOR_BLUE = \033[0;94m
COLOR_GREEN = \033[0;32m
NO_COLOR   = \033[m

##     help:	This.
.PHONY: help
.DEFAULT: help
help: Makefile
#	Find all double comments and treat them as docstrings
	@echo "make <command>"
	@sed -n 's/^##//p' $<


##     fix:	Automatically fix checks (where possible).
.PHONY: fix
fix:
	@echo -e "${COLOR_BLUE}\n=== Black ===\n${NO_COLOR}"
	poetry run black bbfcapi tests

	@echo -e "${COLOR_BLUE}\n=== isort ===\n${NO_COLOR}"
	poetry run isort --recursive bbfcapi tests


##     check:	Run basic checks.
.PHONY: check
check:
	@echo -e "${COLOR_BLUE}\n=== Correctness: Poetry ===\n${NO_COLOR}"
	poetry --quiet check

	@echo -e "${COLOR_BLUE}\n=== Correctness: Pyflakes ===\n${NO_COLOR}"
	poetry run pyflakes bbfcapi tests

	@echo -e "${COLOR_BLUE}\n=== Security: Bandit ===\n${NO_COLOR}"
	poetry run bandit --recursive --quiet bbfcapi

	@echo -e "${COLOR_BLUE}\n=== Security: Safety ===\n${NO_COLOR}"
	poetry run safety check --bare

	@echo -e "${COLOR_BLUE}\n=== Style: Black ===\n${NO_COLOR}"
	poetry run black --quiet --check bbfcapi tests

	@echo -e "${COLOR_BLUE}\n=== Style: isort ===\n${NO_COLOR}"
	poetry run isort --check --recursive bbfcapi tests

	@echo -e "${COLOR_GREEN}\nAll Good!${NO_COLOR}"


##     test:	Run tests.
.PHONY: test
test:
	@echo -e "${COLOR_BLUE}\n=== Pytest ===\n${NO_COLOR}"
	poetry run pytest tests


##     test-live:	Run live integration tests.
.PHONY: test-live
test-live:
	@echo -e "${COLOR_BLUE}\n=== Pytest (inc. live integration tests) ===\n${NO_COLOR}"
	poetry run pytest --run-live tests


##     release:	Do a release.
.PHONY: release
release: check test-live
	git status
	@echo -e "${COLOR_BLUE}\n\nIs your working directory empty?${NO_COLOR}"
	@read -p "Press any key to continue if so..." -n1 -s

	@echo -e "${COLOR_BLUE}\n\nRun 'poetry version major/minor/patch'...${NO_COLOR}"
	@read -p "Press any key to continue when done..." -n1 -s

	@echo -e "${COLOR_BLUE}\n\nUpdate the version in __init__.py and test_bbfcapi.py...${NO_COLOR}"
	@read -p "Press any key to continue when done..." -n1 -s

	@echo -e "${COLOR_BLUE}\n\nUpdate the release notes in README.md...${NO_COLOR}"
	@read -p "Press any key to continue when done..." -n1 -s

	@echo -e "${COLOR_BLUE}\n\nNow about to do the actual release!${NO_COLOR}"
	@read -p "Press any key to continue..." -n1 -s

	@echo -e "\n"
	poetry publish --build
	git commit -am "Release $(shell poetry version)"
	git push


##
##Run make with VERBOSE=1 for additional output.
$(VERBOSE).SILENT:
# Delete targets on failure
.DELETE_ON_ERROR:
