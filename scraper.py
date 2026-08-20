import requests
from bs4 import BeautifulSoup 

# region Conexao no site 
requests.packages.urllib3.disable_warnings()        # Desativa os avisos vermelhos de "Conexão Não Segura" no terminal

url = "https://quotes.toscrape.com/"                # 1.1.1 Definindo a URL do site
resposta = requests.get(url, verify=False)          # 1.1.2 requisição HTTP para obter o conteúdo da página
print("Código de status", resposta.status_code)     # Verificação da requisição
# endregion



# region Raspagem de dados 
soup = BeautifulSoup(resposta.text, "html.parser")  # 1.2.1 Criando o objeto BeautifulSoup para analisar o HTML da página
print("Título da página:", soup.title.text)         #título da página (<title>...</title>)

# Primeira_citacao = soup.find("div", class_= "quote")

# texto = Primeira_citacao.find("span", class_= "text").text
# print("Primeira citação:", texto)

# autor = Primeira_citacao.find("small", class_= "author").text
# print("Autor da citação:", autor)

todas_citacoes = soup.find_all("div", class_= "quote")
print("Quantidade de citações na pagina: ", len(todas_citacoes))
print("")
print("")
# endregion 

for indice, citacao in enumerate(todas_citacoes):
    texto = citacao.find("span", class_= "text").text
    print(f"citação n°{indice + 1}:", texto)

    autor = citacao.find("small", class_= "author").text
    print(f"Autor da citação n°{indice + 1}:", autor)