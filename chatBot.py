
import google.generativeai as genai
from datetime import date
import streamlit as st

API_KEY = "AIzaSyAgHapNvvYUwTVP-GUuIr6Q7XIV6VCLivM"
genai.configure(api_key=API_KEY)

modelo = genai.GenerativeModel("gemini-2.5-flash")

st.title("ChatBot com Gemini + Streamlit")

# Lógica para Gerenciar a Sessão de Chat
if "chat_session" not in st.session_state:
    st.session_state.chat_session = modelo.start_chat(history=[])

# exibe historico rico da Conversa
for message in st.session_state.chat_session.history:
    st.markdown(f"*{'Você' if message.role == 'user' else 'IA'}*: {message.parts[0].text}")

pergunta = st.chat_input("Insira sua pergunta ")
prompt = f"Hoje é {date.today()}. Pergunta: {pergunta}"

if pergunta:
     
 st.markdown(f"*Você*: {pergunta}")
 # manda a resposta da IA para o historico da conversa
 resposta = st.session_state.chat_session.send_message(prompt)
 st.markdown(f"*IA*: {resposta.text}")
