import requests
from bs4 import BeautifulSoup

resposta = requests.get("https://www.google.com/")
html = resposta.content

soup = BeautifulSoup(html, "html.parser")
title = soup.find('title')

print(title)
print(title.string)

resposta.text
