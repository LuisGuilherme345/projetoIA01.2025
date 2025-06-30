import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("estacionamento.csv")

modelo = LinearRegression()
x = df[["tempominu"]]
y = df[["preco"]]

modelo.fit(x, y)

st.title("Prevendo o preço do estacionamento de um shopping baseado em minutos permanecidos")
st.divider()

tempo=st.number_input("Digite a permanência em minutos", min_value=0, step=1, format="%d")

if tempo:
    preco_previsto = modelo.predict([[tempo]])[0][0]
    st.write(f"O valor previsto do estacionamento, com a permanência de {tempo} minutos é de R$ {preco_previsto:.2f}.")