import bs4
import json
import requests
import datetime

def get_table_data(url):
    """Get the url and return the response"""
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
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
        cols = [col.text.strip().replace('\n', ' ') for col in cols]
        cols = cols[:2]
        link.append(cols)
    return link

def save_data(data, filename):
    """Ask the user for the name of the file to save the data"""
    filename = filename + '.json'
    """Save the data in a json file"""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def scrape_data(websites):
    data = {}
    """Get the table data from the website"""
    for i, url in enumerate(websites):
        print(f"Scraping data from {url}, {i+1} of {len(websites)}")
        table_data = get_table_data(url)
        """Add the data to the dictionary with the website's URL as the key"""
        data[url] = table_data
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
