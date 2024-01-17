mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_abs_path := $(subst Makefile,,$(mkfile_path))

build:
	docker build -t geocoding-jupyter .

jupyter:
	docker run \
		-v $(current_abs_path)notebooks:/app/notebooks \
		-v $(current_abs_path)data:/app/data \
		-v $(current_abs_path)utils:/app/utils \
		--name geocoding-app --rm -p 8888:8888 \
		--env-file .env -t geocoding-jupyter jupyter lab \
		--port=8888 --ip='*' --NotebookApp.token='' \
		--NotebookApp.password='' --no-browser --notebook-dir=/app --allow-root