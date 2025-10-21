# Usar a imagem oficial do Python
FROM python:3.9-slim

# Setar o diretório de trabalho no contêiner
WORKDIR /app

# Copiar os arquivos do projeto para dentro do contêiner
COPY . /app

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta 8501 (padrão do Streamlit)
EXPOSE 8501

# Comando para rodar o Streamlit
CMD ["streamlit", "run", "app.py"]
