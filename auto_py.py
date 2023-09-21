import requests
from bs4 import BeautifulSoup

resposta = requests.get("https://www.google.com/")

print(resposta.text)


"""
import requests
from bs4 import BeautifulSoup

header = {'user-agent': 'Mozilla/5.0'}

resposta = requests.get("https://www.google.com/")

html_doc = resposta.text

soup = BeautifulSoup(html_doc, 'html.parser')

for link in soup.find_all('<title>'):
    print(link.get('<title>'))

"""
