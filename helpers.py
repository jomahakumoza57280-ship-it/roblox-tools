import time
import requests
from requests.exceptions import RequestException

def retry_request(func, retries=3, delay=1, *args, **kwargs):
    """Attempt a network request with retry logic."""
    for attempt in range(retries):
        try:
            response = func(*args, **kwargs)
            response.raise_for_status()  # Raise an error for bad responses
            return response
        except RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)  # Wait before retrying
            else:
                raise

# Example usage:
# def fetch_data(url):
#     return requests.get(url)
#
# response = retry_request(fetch_data, url='https://api.example.com/data')
# print(response.json())