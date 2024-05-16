.PHONY: run, lint, format, help

run:  ## Run server on port 8000
	poetry run python manage.py runserver 0.0.0.0:8000

debug:  ## Run server with debugger (django-extensions required)
	poetry run python manage.py runserver_plus 0.0.0.0:8000

DELIM := `seq -s '=' 0 30 | tr -d '[0-9]'`

lint:  ## Do sanity check
	@echo $(DELIM)
	-poetry run djlint . --check
	@echo $(DELIM)
	-poetry run djlint . --lint
	@echo $(DELIM)
	-poetry run black . --check
	@echo $(DELIM)
	-poetry run ruff check .
	@echo $(DELIM)

format:  ## Format your code
	@echo $(DELIM)
	-poetry run djlint . --reformat
	@echo $(DELIM)
	poetry run black .
	@echo $(DELIM)
	poetry run ruff check --fix .
	@echo $(DELIM)

help:  ## Display help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
