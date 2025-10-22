import streamlit as st
import google.generativeai as genai

# chave da API
API_KEY = "AIzaSyAgHapNvvYUwTVP-GUuIr6Q7XIV6VCLivM"
genai.configure(api_key=API_KEY)

# inicia modelo do Gemini
modelo = genai.GenerativeModel("gemini-2.5-flash")

st.title("ChatBot com Gemini + Streamlit")

# Entrada do usuário
pergunta = st.text_input("Você:", "")

if st.button("Enviar") and pergunta.strip() != "":
    # prompt para o modelo
    prompt = f"Pergunta do usuário: {pergunta}"
  # Gerando a resposta usando o modelo
    resposta = modelo.generate_content(prompt)
        
    st.markdown(f"**IA:** {resposta.text}")
    
