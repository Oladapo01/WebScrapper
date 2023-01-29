import bs4
import json
import requests
import datetime
import os
from urllib.parse import urljoin, urlparse

def grab_weblink(url):
    """Get the url and return the response"""
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    """locate the body element"""
    body =soup.find('body')
    """locate all the anchor elements within the website"""
    links = soup.find_all('a')
    internal_links = []
    base_url =urlparse(url).netloc
    for link in links:
        """Extract the href attribute from each anchor element"""
        relative_link = link.get('href')
        full_url = urljoin(url, relative_link)
        internal_links.append(full_url)
    return internal_links

def save_data(data, filename):
    """Ask the user for the name of the file to save the data"""
    filename = filename + '.json'
    """Save the data in a json file"""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def scrape_data(websites):
    data = {}
    """Get website links from the provided Url"""
    for website in websites:
        print(f"Scraping data from {website} completed")
        links = grab_weblink(website)
        """Add the data to the dictionary with the website's URL as the key"""
        data[website] = links
    data['scrapped at'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    save_data(data, file_name)

if __name__ == '__main__':
    websites = []
    while True:
        url = input('Enter the url of the website (Enter q to quit): ')
        if url == 'q':
            break
        else:
            websites.append(url)
    file_name = input('Enter the name of the file to save the data: ')
    scrape_data(websites)