import requests
from bs4 import BeautifulSoup

def extract_author_info(author_url):
    response = requests.get(author_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    author_title = soup.find('h3', class_='author-title').text
    born_date = soup.find('span', class_='author-born-date').text
    born_location = soup.find('span', class_='author-born-location').text
    description = soup.find('div', class_='author-description').text

    return {
        'author_title': author_title,
        'born_date': born_date,
        'born_location': born_location,
        'description': description
    }
