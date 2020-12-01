# Desafio-Neoway
import urllib.request
# Na minha maquina, tive que instalar o bs4, talves você também devera. 
# Abrindo o prompt de comando digite o comando "pip install beautifulsoup4" para realizar a instalação.
from bs4 import BeautifulSoup
import json 

wiki = 'http://www.buscacep.correios.com.br'
wiki_buscar_cep = '/sistemas/buscacep/buscaFaixaCep.cfm'
page = urllib.request.urlopen(wiki + wiki_buscar_cep)

# Se não funcionar esta linha de comando, tende usando html5lib com esta linha de comando "soup = BeautifulSoup(page, 'html5lib')"
soup = BeautifulSoup(page, "lxml")

select = soup.find('select', {'class': 'f1col'})
lista_options = select.find_all('option')

conteudo = []
for lista in lista_options:
    conteudo.append(lista.text)


action = soup.find(id = 'Geral').get('action')

# No caso agora faltaria a parte em que um busco os dados de cada uf,
# estava tentando achar um jeito de chegar até a pagina de resultados de cada uf,
# mas pelo jeito o site dos correios não está abrindo na página de busca da uf, e já faz uns três dias que não consigo abrir.
# Só quero dizer que foi minha primeira experiência com a linguagem Python e que aprendi bastante nesse 
# desafio, pesquisando sobre assuntos que não tinha experiência.
