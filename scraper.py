import requests
from bs4 import BeautifulSoup 

# region Conexao no site 
requests.packages.urllib3.disable_warnings()        # Desativa os avisos vermelhos de "Conexão Não Segura" no terminal

url = "https://quotes.toscrape.com/"                # 1.1.1 Definindo a URL do site
resposta = requests.get(url, verify=False)          # 1.1.2 requisição HTTP para obter o conteúdo da página
print("Código de status", resposta.status_code)     # Verificação da requisição
# endregion


soup = BeautifulSoup(resposta.text, "html.parser")  # 1.2.1 Criando o objeto BeautifulSoup para analisar o HTML da página
print("Título da página:", soup.title.text)         #título da página (<title>...</title>)

Primeira_citacao = soup.find("div", class_="quote")

texto = Primeira_citacao.find("span", class_= "text").text
print("Primeira citação:", texto)