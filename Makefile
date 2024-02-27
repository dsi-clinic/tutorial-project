# Define constants

# General
mkfile_path := $(abspath $(firstword $(MAKEFILE_LIST)))
current_dir := $(notdir $(patsubst %/,%,$(dir $(mkfile_path))))
current_abs_path := $(subst Makefile,,$(mkfile_path))

# Project
project_name := "clinic-workshop-iii"
project_dir := "$(current_abs_path)"

# Read environment variables from file
include .env

# Build Docker image and run containers in different modes
build-only:
	docker build -t $(project_name) -f Dockerfile $(current_abs_path)

run-jupyter:
	docker run \
		-v $(current_abs_path)notebooks:/$(project_name)/notebooks \
		-v $(current_abs_path)data:/$(project_name)/data \
		-v $(current_abs_path)pipeline:/$(project_name)/pipeline \
		--name $(project_name) --rm -p 8888:8888 \
		--env-file .env -t geocoding-jupyter jupyter lab \
		--port=8888 --ip='*' --NotebookApp.token='' \
		--NotebookApp.password='' --no-browser --notebook-dir=/app --allow-root

run-interactive:
	docker build -t $(project_name) -f Dockerfile "$(current_abs_path)"
	docker run -it \
		-v "$(current_abs_path)pipeline":/$(project_name)/pipeline \
		-v "$(current_abs_path)data:"/$(project_name)/data \
		--env-file ".env" \
		-t $(project_name) /bin/bash