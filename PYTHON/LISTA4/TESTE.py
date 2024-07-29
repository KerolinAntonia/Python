import streamlit as st 
 
nome = st.text_input("Digite seu nome: ")
st.write(f"Bem vindo {nome}")

a = st.number_input("n1")
b = st.number_input("n2")

st.write(a+b)