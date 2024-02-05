from quote_search import search_quotes_by_author
from quotes_info import extract_quotes, is_valid_url
from author_info import extract_author_info

if __name__ == "__main__":
    while True:
        print("Options :")
        print("1. Rechercher des citations par auteur")
        print("2. Afficher les citations, auteurs, tags, liens des pages suivantes")
        print("3. Rechercher les informations sur l'auteur par nom")
        print("4. Quitter")
        
        choice = input("Choisissez une option (1/2/3/4) : ")
        
        if choice == '1':
            author_name = input("Entrez le nom de l'auteur : ")
            search_quotes_by_author(author_name)
        elif choice == '2':
            page_url = "https://quotes.toscrape.com"
            while page_url:
                quotes, next_page_url = extract_quotes(page_url)
                for quote in quotes:
                    print(f"Citation : {quote['text']}")
                    print(f"Auteur : {quote['author']}")
                    print(f"Tags : {', '.join(quote['tags'])}\n")
                page_url = next_page_url
        elif choice == '3':
            author_name = input("Entrez le nom de l'auteur pour rechercher les informations : ")
            author_url = f"https://quotes.toscrape.com/author/{author_name.replace(' ', '-').capitalize()}/"
            if is_valid_url(author_url):
                print(f"URL de l'auteur : {author_url}")
                author_info = extract_author_info(author_url)
                print(f"Auteur : {author_name}")
                print(f"Titre de l'auteur : {author_info['author_title']}")
                print(f"Date de naissance : {author_info['born_date']}")
                print(f"Lieu de naissance : {author_info['born_location']}")
                print(f"Description : {author_info['description']}\n")
            else:
                print(f"L'URL de l'auteur est invalide (404 Not Found) : {author_url}")
        elif choice == '4':
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")
