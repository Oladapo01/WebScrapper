# Overview
This is a web scraping program written in Python that can extract internal links from a website and table data from multiple websites. The data is saved in a JSON file.

**Required Libraries**

**The following libraries are used in the program:**

BeautifulSoup

JSON

Requests

Datetime

# How to use
Run the program by executing the script.

Enter the URL of the website you want to scrape.

Enter 'q' to stop entering URLs.

Enter the name of the file to save the data.

# Functions

**grab_weblink(url)**

This function takes a URL as an input and returns a list of all the internal links from the website. It uses the requests library to get the response and bs4 library to parse the HTML.

**get_table_data(url)**

This function takes a URL as an input and returns a list of lists, each inner list contains the data from two td elements within a tr element of a table.

**save_data(data, filename)**

This function takes two arguments, data which is the data to be saved and filename which is the name of the file to save the data. The data is saved in a JSON file.

**scrape_data(websites)**

This function takes a list of URLs as input, gets the internal links from each website using grab_weblink function and gets the table data from each website using the get_table_data function. The data is saved in a JSON file using the save_data function.

# Code Execution
**The code is executed as follows:**

The user is asked to enter the URLs of the websites they want to scrape.

The URLs are stored in a list called websites.

The user is then asked to enter the name of the file to save the data.

The scrape_data function is called with websites as an argument.

The scrape_data function calls grab_weblink and get_table_data functions for each URL in websites.

The data is saved in a JSON file using the save_data function.

# Note
The program is designed to scrape internal links from one website and table data from multiple websites. It may not work as expected on all websites, as websites can have different structures. The user may need to modify the code to scrape data from specific websites.
