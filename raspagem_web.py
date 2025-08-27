# //Raspagem da web
# //Vou extrair dados de sites automaticamente

# Passos:
""" 1.Rastreamento - Acesso do site via link
    2.Extração - Extração dos dados desejados do codigo html da pág.
    3.Armazenamento - Os dados são armazenados uma planilha, banco de dados ou arquivo CSV
"""

# //Bibliotecas necessarias
import requests as rs  # Requisição
from bs4 import BeautifulSoup as bs  # Extração
import pandas as pd  # Armazenar em tabela

# loops das pag(1-50)
livros = []

for pag in range(1, 51):
    if pag == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{pag}.html"

# Requisição
    response = rs.get(url)
    # print(response) ta funcionando
    site = bs(response.text, 'html.parser')
    # print(site.prettify()) ta funcionando

# scrapping
    '''
Titulos: <h3>
Preços: class="price_color"
Disponivel: class="instock availability"

    '''
    titulo = site.find_all('h3')
    Preco = site.find_all(class_="price_color")
    Disp = site.find_all(class_="instock availability")

# Estrutura dos dados
    for t, p, d in zip(titulo, Preco, Disp):
        nome = t.a['title']
        preco = p.text.replace("Â£","£")
        Disponibilidade = d.text.strip()
        livros.append([nome, preco, Disponibilidade])

# Criando tabela
df = pd.DataFrame(livros, columns=['Titulo', 'Preço', 'Disponibilidade'])

# Salvando em um arquivo csv
df.to_csv("Tabela_de_livros.csv", index=False)
