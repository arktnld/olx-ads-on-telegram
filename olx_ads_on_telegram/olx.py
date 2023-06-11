import requests, re
from bs4 import BeautifulSoup
import pdb
#
# Code to get ads from https://olx.com.br
#

def request_ads(url, patterns):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    # Faça uma solicitação GET para o site e armazene a resposta em uma variável
    response = requests.get(url, headers=headers)

    urls = []

    # Verifique se a solicitação foi bem-sucedida (código de status 200 indica sucesso)
    if response.status_code == 200:
        # Extraia o conteúdo HTML da resposta
        html_content = response.content

        # Crie um objeto BeautifulSoup para analisar o conteúdo HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Encontre todas as tags <a> que contêm um atributo href
        links = soup.find_all('a', href=True)

        # Defina o padrão que corresponde aos valores que você deseja obter
        pattern = 'https:\/\/df\.olx\.com.br\/distrito-federal-e-regiao.*'

        # Imprima todas as URLs encontradas
        # n = 0
        for link in links:
            match = re.search(pattern, link['href'])
            if match:
                out = match.group()

                for pttrn in patterns:
                    found = re.search(pttrn, out)

                    if found:
                        # print(out)
                        urls.append(out)

    else:
        print("Não foi possível pegar as URLs do site.")

    return urls


# Get info from ods of https://olx.com.br
def request_info(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

   # Faça uma requisição GET para obter o conteúdo da página
    response = requests.get(url, headers=headers)
    print(url)

   # Use o BeautifulSoup para analisar o HTML da página
    soup = BeautifulSoup(response.content, 'html.parser')

    price = soup.find_all(['h1', 'h2'])[0].get_text()
    if price == "A página não foi encontrada...": return None

    # title = soup.find_all(['h1', 'h2'])[1].get_text()
    # cep = soup.find_all(['dd'])[0].get_text()
    # state = soup.find_all(['dd'])[1].get_text()
    # city = soup.find_all(['dd'])[2].get_text()
    # info = [s.replace('&', '') for s in [ price, url]]
    #
    return [ price, url ]

