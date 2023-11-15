mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_abs_path := $(subst Makefile,,$(mkfile_path))

create-config:
	@echo '{' > $(current_abs_path)/config.json
	@echo '  "data_path": "$(current_abs_path)data/",' >> $(current_abs_path)/config.json
	@echo '  "notebooks_path": "$(current_abs_path)notebooks/"' >> $(current_abs_path)/config.json
	@echo '}' >> $(current_abs_path)/config.json

build:
	docker build -t example-container .

jupyter:
	docker run -v $(current_abs_path):/app --name example-app --rm -p 8888:8888 --env-file .env -t example-container jupyter lab --port=8888 --ip='*' --NotebookApp.token='' --NotebookApp.password='' --no-browser --notebook-dir=/app --allow-root