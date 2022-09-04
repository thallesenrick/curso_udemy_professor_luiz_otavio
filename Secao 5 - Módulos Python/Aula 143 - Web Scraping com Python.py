import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.s-post-summary js-post-summary'):
    titulo = pergunta.select_one('.s-link')
    data = pergunta.select_one('.relativetime')
    voto = pergunta.select_one('.s-post-summary--stats-item-unit')
    print(f'Data do post: {data.text}')
    print(f'Titulo do post: {titulo.text}')
    print(f'Votos do post: {voto.text}')
