"""Functions for geocoding addresses and coordinates.
"""

import json
import os
import requests

BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places/"


def geocode_address(
    street: str = None,
    city: str = None,
    state: str = None,
    zip: str = None,
    full_address: str = None,
) -> tuple[float, float]:
    """Geocodes an address using the Mapbox API.

    A variety of formats for addresses work here since the Mapbox API is pretty
    smart with how it parses stuff. You can, for example, give a specific
    address or you can give only a city like "Chicago".

    Args:
        street: Street address (i.e. "123 Fake Street")
        city: City name
        state: State name. This can be the full state name or the abbreviation
        zip: Zip code. This must be a string!
        full_address: a whole address merged together. Will be used in place
            of other options if provided.

    Returns:
        A tuple of latitude and longitude. These are returned as floats. For
        example: (-41.8781, 87.6298).
    """
    # Fetch Mapbox API token from environment variables
    try:
        token = os.environ["MAPBOX_ACCESS_TOKEN"]
    except KeyError as e:
        raise RuntimeError(
            f"Required environment variable {e} is missing or empty."
        ) from None

    # Build request URL
    if full_address:
        address = full_address
    else:
        address = f"{street} {city} {state} {zip}"
    url = f"{BASE_URL}{address}.json?access_token={token}"

    # Send request and handle any non-success response
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(
            f"The API request failed with a {r.status_code}-{r.reason} "
            f'status code and the text "{r.text}".'
        )

    # Parse latitude and longitude from response body
    try:
        lng, lat = r.json()["features"][0]["center"]
    except (json.JSONDecodeError, KeyError, IndexError) as e:
        raise RuntimeError(
            "Unable to parse latitude and longitude from response body JSON."
            "The JSON was not shaped as expected, so the API may have "
            f'been recently updated: "{e}".'
        ) from None

    return lat, lng
