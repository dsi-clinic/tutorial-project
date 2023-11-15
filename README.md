# Tutorial Project

This is the cleaned up version of a tutorial project.

This project involves geocoding addresses from an Excel file that contains Food Safety and Inspection (FSIS) data for poultry processing plants using the Mapbox API.

## Running the Geocoding Notebook

To geocode our addresses, we will use a Jupyter notebook that is running in a Docker container.

1. **Mapbox API Key**: We need a `.env` file located in the root of our directory that includes a `MAPBOX_API_KEY` variable. If you don't already have a Mapbox API key, sign up for a free account at https://account.mapbox.com and get your API key.

2. **FSIS Data**: The script expects there to be a file called `MPI_Directory_by_Establishment_Number.xlsx` located in a `data` folder in the root of the directory. You can (download the example data from Google Drive here)[https://docs.google.com/spreadsheets/d/1swbQmuix-tCRBPK2wizncPLmrlWBgR-g/edit?usp=drive_link&ouid=114633865943391212776&rtpof=true&sd=true].

3. **Create Config File**: We dynamically create a `config.json` that handles filepaths for this project by running `make create-config`

4. **Build Docker Image**: Build the Docker image for this project by running `make build`

5. **Start a Docker Container with a Jupyter Server**: Run `make jupyter`. Copy and paste the url that looks something like `localhost:0000` into your browser. This should open a Jupyter server where you can run the `geocode-clean.ipynb` notebook

6. **Follow the Notebook Instructions**: The notebook imports a script from `utils/geocode.py` and outputs a CSV file that now includes a latitude and longitude for each plant.