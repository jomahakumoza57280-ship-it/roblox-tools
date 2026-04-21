import requests
import time
import logging

def retry_request(url, max_retries=3, delay=2):
    """
    Perform a network request with retry logic.
    Retries the request on failure up to max_retries.
    """
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise error for bad responses
            return response.json()  # Return JSON response
        except requests.exceptions.RequestException as e:
            attempts += 1
            logging.warning(f'Request failed: {e}. Attempt {attempts} of {max_retries}.')
            if attempts < max_retries:
                time.sleep(delay)  # Wait before retrying
            else:
                logging.error('Maximum retries exceeded.')
                raise

# Example usage:
if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except Exception as error:
        logging.error(f'Failed to retrieve data: {error}')