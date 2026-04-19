import time
import requests
from requests.exceptions import ConnectionError, Timeout, HTTPError

class MaxRetriesExceeded(Exception):
    pass

def retry(func, max_retries=3, delay=2, *args, **kwargs):
    attempts = 0
    while attempts < max_retries:
        try:
            return func(*args, **kwargs)
        except (ConnectionError, Timeout, HTTPError) as e:
            attempts += 1
            print(f"Attempt {attempts} failed: {e}")
            if attempts >= max_retries:
                raise MaxRetriesExceeded(f'Max retries exceeded for {func.__name__}')
            time.sleep(delay)

# Example network operation

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

# Usage of the retry decorator

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry(fetch_data, max_retries=5, delay=3, url=url)
        print(data)
    except MaxRetriesExceeded as e:
        print(e)
