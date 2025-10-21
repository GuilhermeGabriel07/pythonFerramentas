# só funciona o streamlit no vscode

import streamlit as st
#pip install streamlit

import google.generativeai as genai
#pip install google-generativeai

API_KEY = "AIzaSyAgHapNvvYUwTVP-GUuIr6Q7XIV6VCLivM"
genai.configure(api_key=API_KEY)

# modelo do gemini
modelo = genai.GenerativeModel("gemini-2.5-flash")

# Armazena o chat para melhores interações
if "chat" not in st.session_state:
    st.session_state.chat = modelo.start_chat(history=[])


st.title("ChatBot com Gemini + Streamlit")

pergunta = st.text_input("Você:", "")

if st.button("Enviar") and pergunta.strip() != "":
    resposta = st.session_state.chat.send_message(pergunta)
    st.markdown(f"**IA:** {resposta.text}")
