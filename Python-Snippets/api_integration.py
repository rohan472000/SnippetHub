"""
* API Integration *

API integration refers to the process of connecting two or more applications or systems by using APIs (Application Programming Interfaces). 
Exchange data and perform actions. APIs are sets of protocols and standards that allow different, 
software applications to communicate with each other.

Wikipedia: https://en.wikipedia.org/wiki/API

"""

import requests
from typing import Optional, Dict, Any


def make_api_request(url: str, 
                     method: str = 'GET', 
                     params: Optional[Dict[str, Any]] = None, 
                     data: Optional[Dict[str, Any]] = None, 
                     headers: Optional[Dict[str, str]] = None) -> Optional[Dict[str, Any]]:
    """
    Send an HTTP request to the specified API endpoint.

    Args:
        url (str): The URL of the API endpoint.
        method (str, optional): The HTTP method to use (default is 'GET').
        params (Dict, optional): Optional query parameters for the request.
        data (Dict, optional): Optional data to include in the request body.
        headers (Dict, optional): Optional headers to include in the request.

    Returns:
        Optional[Dict, None]: Parsed JSON response if the request is successful, None otherwise.

    Raises:
        requests.exceptions.RequestException: If an error occurs while making the request.
    """
    try:
        # Send an HTTP request to the API endpoint with optional headers, parameters, and data
        response = requests.request(method, url, params=params, data=data, headers=headers,)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            return data
        else:
            # Handle non-200 status codes gracefully
            print(f'API request failed with status code {response.status_code}. Reason: {response.text}')
            return None

    except requests.exceptions.RequestException as e:
        # Handle any request exceptions
        print(f'Error making the API request: {e}')
        return None

if __name__ == '__main__':
    api_url = 'https://api.github.com/users/prasad-chavan1'  # Replace with the API URL you want to fetch
    http_method = 'GET'  # You can change the HTTP method as needed (e.g., 'POST', 'PUT', 'DELETE')
    
    response_data = make_api_request(api_url, method=http_method)

    if response_data is not None:
        print("Received Data:")
        print(response_data)
    else:
        print("No data received. Check the API request for errors.")