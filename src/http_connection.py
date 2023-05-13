import requests
import logging
import os

def save_endpoint_response(endpoint, extension='', path=''):
    """
    Downloads an HTTP response and saves it to disk.
    :param endpoint: The URL to download.
    :param path: Optional path to save the file to. If not provided, the file will be saved to the current working directory.
    :return: None
    """
    try:
        # Send request toe the endpoint
        response = requests.get(endpoint)
        logging.debug(f"HTTP request sent to {endpoint}")

        # Add the filename and extension to path
        filepath = ".".join([endpoint.split("/")[-1], extension])
        filepath = os.path.join(path,filepath)

        # Save the response to disk
        with open(filepath, "wb") as f:
            f.write(response.content)
        logging.debug(f"HTTP response saved to {filepath}")

    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to download {endpoint}: {e}")
    except PermissionError as e:
        logging.error(f"Failed to lock file for writing: {e}")