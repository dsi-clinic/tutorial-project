# Tutorial Project

This is the cleaned up version of a tutorial project.

This project involves geocoding addresses from an Excel file that contains Food Safety and Inspection (FSIS) data for poultry processing plants using the Mapbox API.

## Running the Geocoding Notebook

To geocode our addresses, we will use a Jupyter notebook that is running in a Docker container.

1. **Mapbox API Key**: We need a `.env` file located in the root of our directory that includes a `MAPBOX_TOKEN` variable. If you don't already have a Mapbox API key, sign up for a free account at https://account.mapbox.com. Once you're logged in, copy your defaault public access token into the `.env` file (e.g., `MAPBOX_TOKEN=pk.<...>`). (_Note: To avoid a [current Docker bug](https://stackoverflow.com/questions/30494050/how-do-i-pass-environment-variables-to-docker-containers/75237297#75237297), no quotation marks should be used around the token value._)

1. **FSIS Data**: The script expects there to be a file called `MPI_Directory_by_Establishment_Number.xlsx` located in a `data/raw/` folder in the root of the directory. You can [download the example data from Google Drive here](https://docs.google.com/spreadsheets/d/1swbQmuix-tCRBPK2wizncPLmrlWBgR-g/edit?usp=drive_link&ouid=114633865943391212776&rtpof=true&sd=true).

1. **Build Docker Image**: Build the Docker image for this project by running `make build`.

1. **Start a Docker Container with a Jupyter Server**: Run `make jupyter`.

1. **Access JupyterLab** Copy and paste the url that looks something like [http://localhost:8888/lab](http://localhost:8888/lab) into your browser. This should open a Jupyter Lab server where you can run the `geocode-clean.ipynb` notebook (located in the `notebooks` directory)

1. **Follow the Notebook Instructions**: The notebook imports a script from `utils/geocode.py` and outputs a CSV file that now includes a latitude and longitude for each plant.

## Notes

### Makefile

For projects that require Docker commands with lots of arguments or require running certain sequences of shell scripts to prepare data files, it's common practice to use a [Makefile](https://web.stanford.edu/class/archive/cs/cs107/cs107.1174/guide_make.html) to standardize these commands. It makes it easy for new users to repeat the exact commands they need to get a working version of the project up and running.

### Docker

[Containerization](https://www.docker.com/resources/what-container/) makes code more reproducible and is industry standard for deploying applications.

While setup for Docker can be finicky, if your code runs correctly in a Docker container, it makes it _much_ more likely that future users will be able to use your code without running into frustrating environment issues.

In this example, we have a Docker image that is set up to run a JupyterLab server.

If you're curious, you can examine the Docker commands in more detail in the `Makefile`.

One of the key things to notice is that the local file system is [mounted as a volume](https://docs.docker.com/storage/volumes/) so that changes in the Docker container will be saved locally.

Also, making the containerized Jupyter Lab server accessible from your local machine requires a lot of extra flags to prevent authorization errors. You can see in the details in the `make jupyter` command.

### Installing Scripts as a Package

When dealing with both scripts and notebooks, it can be difficult to properly import scripts into your notebooks.

A common solution you'll find online is to do hacky things to append different folders to your [PATH](https://askubuntu.com/questions/551990/what-does-path-mean).

This is fine for a quick workaround to test things out, but a better solution is to install your scripts as a package so you can import it like this: `from scripts import good_function`

### .gitignore

In general, we want to avoid committing data files to Git repos. We also want to avoid committing sensitive information like API keys or random system files like `.DS_Store`. The `.gitignore` file is a list of files and directories that Git will, you guessed it, _ignore_.

In this project, we've ignored the entire `data` folder as well as our `.env` file. Since we are ignoring our `.env` file and our `data` folder, we should make sure that the README tells users what files they will manually need to add to their directory to run our code.