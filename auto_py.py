import requests
from bs4 import BeautifulSoup
import time

def name():
    global link
    print("Escreva a URL do site:")
    link = input()

def request():
    global resposta
    global html
    try:
        resposta = requests.get(link)
        html = resposta.content
    except:
        print("URL não encontrada")

def soupa():
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find('title')
    time.sleep(1.5)
    print(title.string)
    time.sleep(1.5)
    resposta.text

while True:
    try:
        name()
    except:
        break

    try:
        request()
    except:
        break

    try:
        soupa()
    except: break
