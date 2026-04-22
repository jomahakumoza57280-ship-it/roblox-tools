import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, delay=2):
    """Attempts to perform a network request with retries.

    Args:
        url (str): The URL to send the request to.
        max_retries (int): Maximum number of retries.
        delay (int): Delay between retries in seconds.

    Returns:
        response: The response object from the request.
    """
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an exception for HTTP errors
            return response
        except RequestException as e:
            attempts += 1
            print(f'Attempt {attempts} failed: {e}')
            if attempts < max_retries:
                time.sleep(delay)
            else:
                print('Max retries reached. Exiting.')
                raise
    return None
