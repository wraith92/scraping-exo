from quotes_info import extract_quotes, is_valid_url
from author_info import extract_author_info

def search_quotes_by_author(author_name):
    base_url = "http://quotes.toscrape.com"
    page_url = base_url
    found_author = False

    while page_url:
        quotes, next_page_url = extract_quotes(page_url)
        for quote in quotes:
            if author_name.lower() in quote['author'].lower():
                if not found_author:
                    if quote['author_link'] is not None:
                        author_url = base_url + quote['author_link']
                        author_info = extract_author_info(author_url)
                        print(f"Auteur : {author_info['author_title']}")
                        print(f"Date de naissance : {author_info['born_date']}")
                        print(f"Lieu de naissance : {author_info['born_location']}")
                        print(f"Description : {author_info['description']}\n")
                        found_author = True
                    else:
                        print(f"Auteur : {author_name}")
                        print("Aucune information sur l'auteur trouvée.\n")
                        found_author = True
                
                print(f"Citation : {quote['text']}")
                print(f"Tags : {', '.join(quote['tags'])}\n")

        if not found_author:
            print(f"Aucune citation trouvée pour l'auteur : {author_name}")

        page_url = next_page_url
