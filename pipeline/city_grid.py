"""Plots a city against a grid.
"""

# Standard library imports
import os
import json

# Third-party imports
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import shape

# Application imports
from utils.geometry import BoundingBox


def main() -> None:
    """Loads a city boundary file, divides that city into
    smaller "cells", and saves the result to an output file.

    Args:
        `None`

    Returns:
        `None`
    """
    # Load GeoJSON file and extract city geometry
    with open("../data/boundaries/galveston.geojson") as f:
        geometry = json.load(f)["features"][0]["geometry"]

    # Convert geometry to Shapely Polygon or MultiPolygon and get bounds
    city = shape(geometry)
    min_x, min_y, max_x, max_y = city.bounds

    # Create bounding box from coordinates
    bbox = BoundingBox(min_x=min_x, max_x=max_x, min_y=min_y, max_y=max_y)

    # Store all geographies in list
    geos = [city]

    # Split bounding box into smaller "cells" along its x- and y-axes, adding to list
    for cell in bbox.split_along_axes(x_into=5, y_into=5):
        geos.append(cell.to_shapely())

    # Convert geographies to GeoDataFrame
    gdf = gpd.GeoDataFrame(geometry=geos, crs="EPSG:4326")
    print("Total number of geos:", len(gdf))

    # Plot geographies and save result to output file
    gdf.plot(facecolor="none")
    os.makedirs("../data/outputs", exist_ok=True)
    plt.savefig("../data/outputs/galveston.jpg")


if __name__ == "__main__":
    main()
