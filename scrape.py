import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    #Requests pulls html data
    page = requests.get(url)

    #BS4 parses HTML data
    soup = BeautifulSoup(page.content, 'html.parser')

    #Find all the UL elements
    ul_elements = soup.find_all('ul')

    #Finds li items
    fortunes = ul_elements[1].find_all('li')

    #Removes the tags
    fortunes_cleaned = []
    for fortune in fortunes:
        fortunes_cleaned.append(fortune.get_text())
    return fortunes_cleaned

    


