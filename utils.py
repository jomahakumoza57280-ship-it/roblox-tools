import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, backoff=1):
    """Perform a GET request with retry logic on failure."""
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON content if successful
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                time.sleep(backoff * (2 ** attempt))  # Exponential backoff
            else:
                raise NetworkError(f'Failed to fetch from {url} after {retries} retries') from e

# Example usage
if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except NetworkError as ne:
        print(ne)