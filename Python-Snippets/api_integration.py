"""
* API Integration *

API integration refers to the process of connecting two or more applications or systems by using APIs (Application Programming Interfaces). 
Exchange data and perform actions. APIs are sets of protocols and standards that allow different, 
software applications to communicate with each other.

Wikipedia: https://en.wikipedia.org/wiki/API

"""

import requests

# URL of the API endpoint
api_url = 'https://api.github.com/users/prasad-chavan1'

try:
    # Send an HTTP GET request to the API endpoint
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Process the data (e.g., print it)
        print("Received Data:")
        print(data)
    else:
        print('Failed to retrieve data from the API. Status code:', response.status_code)

except requests.exceptions.RequestException as e:
    print('Error making the API request:', e)
