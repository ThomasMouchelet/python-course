import requests
from bs4 import BeautifulSoup

# Faire une requête GET pour le site web
response = requests.get('https://news.ycombinator.com/')

# Parser le contenu de la page avec Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Trouver tous les éléments 'a' avec la classe 'storylink'
storylinks = soup.select('span.titleline a')

# Boucler sur chaque lien et imprimer le texte du lien (le titre du post)
for link in storylinks:
    print(link.text)