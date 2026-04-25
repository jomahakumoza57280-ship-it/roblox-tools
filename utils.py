import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, max_retries=3, delay=1, backoff=2):
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            attempt += 1
            if attempt >= max_retries:
                raise NetworkError(f'Failed after {max_retries} attempts') from e
            time.sleep(delay)
            delay *= backoff
