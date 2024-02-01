# Pull base Docker image
# https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-scipy-notebook
FROM quay.io/jupyter/scipy-notebook

# Create working directory
WORKDIR /app

# Install packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install utils as a package in editable mode
COPY setup.py .
COPY utils ./utils
RUN pip install -e .