import requests
from bs4 import BeautifulSoup

def extract_quotes(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = []

    for quote_div in soup.find_all('div', class_='quote'):
        text = quote_div.find('span', class_='text').get_text()
        author = quote_div.find('small', class_='author').get_text()
        author_link = quote_div.find('small', class_='author').find('a', href=True)
        if author_link:
            author_link = author_link['href']
        else:
            author_link = None

        tags = [tag.get_text() for tag in quote_div.find_all('a', class_='tag')]

        quotes.append({
            'text': text,
            'author': author,
            'author_link': author_link,
            'tags': tags
        })

    next_page_link = soup.find('li', class_='next')
    if next_page_link:
        next_page_link = next_page_link.find('a', href=True)
        if next_page_link:
            next_page_url = page_url.split('/page/')[0] + next_page_link['href']
        else:
            next_page_url = None
    else:
        next_page_url = None

    return quotes, next_page_url

def is_valid_url(url):
    response = requests.head(url)
    return response.status_code == 200
