import requests
import json
import time

# rate limit Vars
MAX_RETRIES = 5
RETRY_DELAY = 1  # seconds
TIMEOUT = 10 # seconds


def safe_request(url, params=None):
    """
    Makes a GET request to the specified URL with optional parameters.
    Implements retry logic for handling rate limits and timeouts.
    """
    retries = 0
    headers = {"User-Agent": "GameHub/1.0"}
    while retries < MAX_RETRIES:
        try:
            response = requests.get(url, params=params, headers=headers, timeout=TIMEOUT)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}. Retrying in {RETRY_DELAY} seconds...")
            retries += 1
            time.sleep(RETRY_DELAY)
    raise Exception(f"Failed to fetch data from {url} after {MAX_RETRIES} retries.")