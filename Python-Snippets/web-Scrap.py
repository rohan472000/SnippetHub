"""
* Web Scraping in Python *

Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites. 
Web scraping software may directly access the World Wide Web using the Hypertext Transfer Protocol or a web browser.

Wikipedia : https://en.wikipedia.org/wiki/Web_scraping
"""
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://en.wikipedia.org/wiki/Web_scraping'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all the article titles using the appropriate HTML tags and attributes
    article_titles = soup.find_all('p')
    
    # Print the titles of the articles
    for title in article_titles:
        print(title.text)
else:
    print('Failed to retrieve the web page. Status code:', response.status_code)
