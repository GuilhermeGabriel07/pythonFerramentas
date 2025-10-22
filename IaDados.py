import pandas as pd
import google.generativeai as genai

# Carregar os dados
dados = pd.read_excel('pythonWeb/produtos.xlsx')

# Exemplo de pergunta sobre os dados
pergunta = "Quantas vendas foram feitas?"

# Criar uma string com os dados para passar para o modelo
dados_str = dados.to_string(index=False)

# Configuração do modelo
API_KEY = "AIzaSyAgHapNvvYUwTVP-GUuIr6Q7XIV6VCLivM"
genai.configure(api_key=API_KEY)
modelo = genai.GenerativeModel("gemini-2.5-flash")

# Criar o prompt com os dados e a pergunta
prompt = f" Não usar linguagem Markdown nem acentuação, não escrever  numero por extenço.Dados de vendas e avaliações de produtos:\n{dados_str}\n\nPergunta: {pergunta}"

resposta = modelo.generate_content(prompt)

print("Resposta gerada pela IA:",resposta.text)
