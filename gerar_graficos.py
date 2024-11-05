import matplotlib.pyplot as plt
import requests
import os

# Função para buscar dados dos repositórios via API do GitHub
def get_repos_data():
    url = 'https://api.github.com/users/DalPra0/repos'
    response = requests.get(url)
    repos = response.json()
    languages = {}
    
    for repo in repos:
        lang_url = repo['languages_url']
        lang_response = requests.get(lang_url)
        for lang, count in lang_response.json().items():
            languages[lang] = languages.get(lang, 0) + count
    
    return languages, len(repos)

# Função para gerar gráficos
def generate_graphics():
    languages, num_repos = get_repos_data()
    
    # Gráfico de Barras
    plt.figure(figsize=(10, 6))
    plt.bar(languages.keys(), languages.values(), color='skyblue')
    plt.title('Quantidade de Projetos por Linguagem')
    plt.savefig('imagens/grafico_barras.png')
    
    # Gráfico de Pizza
    plt.figure(figsize=(8, 8))
    plt.pie(languages.values(), labels=languages.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Distribuição de Linguagens')
    plt.savefig('imagens/grafico_pizza.png')

# Criar pasta de imagens caso não exista
if not os.path.exists('imagens'):
    os.makedirs('imagens')

generate_graphics()
