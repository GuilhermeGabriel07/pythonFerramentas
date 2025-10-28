import google.generativeai as genai
from datetime import date
import streamlit as st

# Configuração da chave da API
API_KEY = "AIzaSyAgHapNvvYUwTVP-GUuIr6Q7XIV6VCLivM"
genai.configure(api_key=API_KEY)

# Inicia o modelo do Gemini
modelo = genai.GenerativeModel("gemini-2.5-flash")
st.title("ChatBot com Gemini + Streamlit")
pergunta = st.chat_input("Você: ")
usuario = st.markdown(f'**Você**: {pergunta}')
if  pergunta != 'cancelar':
    
    prompt = f"Hoje é dia {date.today()}. Pergunta do usuário: {pergunta}"
    resposta = modelo.generate_content(prompt)
    if resposta :
     st.markdown(f"\r**IA:** {resposta.text}")
    
