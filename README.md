# Tutorial Project

This is the cleaned up version of a tutorial project.

This project involves geocoding addresses from an Excel file that contains Food Safety and Inspection (FSIS) data for poultry processing plants using the Mapbox API.

## Running the Geocoding Notebook

To geocode our addresses, we will use a Jupyter notebook that is running in a Docker container.

1. **Mapbox API Key**: We need a `.env` file located in the root of our directory that includes a `MAPBOX_API_KEY` variable. If you don't already have a Mapbox API key, sign up for a free account at https://account.mapbox.com and get your API key.

2. **FSIS Data**: The script expects there to be a file called `MPI_Directory_by_Establishment_Number.xlsx` located in a `data/raw/` folder in the root of the directory. You can (download the example data from Google Drive here)[https://docs.google.com/spreadsheets/d/1swbQmuix-tCRBPK2wizncPLmrlWBgR-g/edit?usp=drive_link&ouid=114633865943391212776&rtpof=true&sd=true].

3. **Create Config File**: We dynamically create a `config.json` that handles filepaths for this project by running `make create-config`

4. **Build Docker Image**: Build the Docker image for this project by running `make build`

5. **Start a Docker Container with a Jupyter Server**: Run `make jupyter`. Copy and paste the url that looks something like `http://localhost:8888/lab` into your browser. This should open a Jupyter Lab server where you can run the `geocode-clean.ipynb` notebook

6. **Follow the Notebook Instructions**: The notebook imports a script from `utils/geocode.py` and outputs a CSV file that now includes a latitude and longitude for each plant.

## Notes

### Makefile

For projects that require Docker commands to set up or require running certain sequences of shell scripts to prepare data files, it's common practice to use a Makefile to standardize these commands. It makes it easy for new users to repeat the exact commands they need to get a working version of the project up and running.

### Docker

[Containerization](https://www.docker.com/resources/what-container/) makes code more reproducible and is also a very common setup for applications that are actually deployed.

While setup for Docker can be finicky, if your code runs correctly in a Docker container, it makes it *much* more likely that future users will be able to use your code without running into frustrating environment issues.

In this example, we have a Docker image that is set up to run a Jupyter server. The Make commands show some of the details, but some of the key things to notice is that the local file system is (mounted as a volume)[https://docs.docker.com/storage/volumes/] so that changes in the Docker container will be saved locally.

There are also a bunch of flags added to the `docker run` command that enable us to access the Jupyter server that is running in the Docker container without hitting a bunch of authorization issues.

### Installing Scripts as a Package

When dealing with both scripts and notebooks, it can be difficult to properly import scripts into your notebooks.

A common solution you'll find online is to do hacky things to append different folders to your (PATH)[https://askubuntu.com/questions/551990/what-does-path-mean]. 

This is fine for a quick work around to test things out, but the solution to this to make your code cleaner and more reproducible is to install your scripts as a package so you can do more standard looking Python imports like `from scripts import good_function`

### .gitignore

In general, we want to avoid committing data files to Git repos. We also want to avoid committing sensitive information like API keys or random system files like `.DS_Store`. The `.gitignore` file is a list of files and directories that Git will, surprisingly enough, ignore.

In this project, we've ignored the entire `data` folder as well as our `.env` file. The instructions in this README give future users instructions on how to download data and tell them to create a `.env` file with the required API key.
