from bs4 import BeautifulSoup
import requests


# Urls
serebii_page = 'https://www.serebii.net/pokemon/gen1pokemon.shtml'

# Parser
soup = BeautifulSoup(requests.get(serebii_page).text, 'html.parser')

print(soup.findAll())


