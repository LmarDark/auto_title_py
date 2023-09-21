import requests
from bs4 import BeautifulSoup

print("Em quantas URLs deseja retirar o title")
res = int(input())

for i in range(res):
    print("Escreva o site")
    link = input()

    resposta = requests.get(link)
    html = resposta.content

    soup = BeautifulSoup(html, "html.parser")
    title = soup.find('title')

    print(title)
    print(title.string)

    resposta.text
