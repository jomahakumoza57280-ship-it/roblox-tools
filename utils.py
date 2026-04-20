import time
import requests

class NetworkException(Exception):
    pass

def retry_network_operation(max_retries=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except (requests.ConnectionError, requests.Timeout) as e:
                    retries += 1
                    if retries == max_retries:
                        raise NetworkException(f'Network operation failed after {max_retries} attempts')
                    time.sleep(delay)
        return wrapper
    return decorator

@retry_network_operation(max_retries=5, delay=1)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()