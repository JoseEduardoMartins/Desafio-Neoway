import urllib.request
from bs4 import BeautifulSoup
import json 

wiki = 'http://www.buscacep.correios.com.br'
wiki_buscar_cep = '/sistemas/buscacep/buscaFaixaCep.cfm'
page = urllib.request.urlopen(wiki + wiki_buscar_cep)
soup = BeautifulSoup(page, "lxml")

select = soup.find('select', {'class': 'f1col'})
lista_options = select.find_all('option')

conteudo = []
for lista in lista_options:
    conteudo.append(lista.text)


action = soup.find(id = 'Geral').get('action')

    
