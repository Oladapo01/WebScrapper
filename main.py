import bs4 as BeautifulSoup
import json
import requests
import datetime

def get_table_data(url):
    """Get the url and return the response"""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    """locate the table element"""
    table =soup.find('table')
    """locate all the table row element within the table"""
    rows = table.find_all('tr')
    # create an empty list to store the data
    link = []
    for row in rows:
        """locate all the td element within the tr element"""
        cols = row.find_all('td')
        """Extract the the text from each td element"""
        cols = [col.text.strip() for col in cols]
        link.append(cols)
    return link

def save_data(data, filename):
    """Save the data in a json file"""
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)


def scrape_data(urls):
    data = {}
    for website in websites:
        """Get the table data from the website"""
        table_data = get_table_data(website)
        """Add the data to the dictionary with the website's URL as the key"""
        data[website] = table_data
    data['scrapped at'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    save_data(data, 'data.json')

if __name__ == '__main__':
    websites = []
    scrape_data(websites)
