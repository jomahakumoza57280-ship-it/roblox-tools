import time
import requests
from requests.exceptions import RequestException

class NetworkOperation:
    MAX_RETRIES = 3
    WAIT_TIME = 2  # seconds

    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        attempt = 0
        while attempt < self.MAX_RETRIES:
            try:
                response = requests.get(self.url)
                response.raise_for_status()  # Raise an error for bad responses
                return response.json()
            except RequestException as e:
                attempt += 1
                print(f"Attempt {attempt} failed: {e}")
                if attempt < self.MAX_RETRIES:
                    print(f"Retrying in {self.WAIT_TIME} seconds...")
                    time.sleep(self.WAIT_TIME)
                else:
                    print("All attempts failed.")
                    raise

# Example usage
if __name__ == '__main__':
    operation = NetworkOperation('https://api.example.com/data')
    try:
        data = operation.fetch_data()
        print(data)
    except Exception as e:
        print(f"Failed to fetch data: {e}")
