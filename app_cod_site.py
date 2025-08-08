import streamlit as st
import pickle
import pandas as pd

# Carregando o modelo
with open('modelo_fraude.pkl', 'rb') as f:
    modelo = pickle.load(f)

# Função para fazer previsões
def fazer_previsao(dados):
    previsao = modelo.predict(dados)
    return previsao[0]

# Interface gráfica
st.title("Detecção de Fraude")
st.write("Este aplicativo detecta transações fraudulentas com base em dados históricos.")

# Campos para entrada de dados
valor_transacao = st.number_input("Valor da Transação", min_value=0)
tempo_conta = st.number_input("Tempo da Conta (meses)", min_value=0)
num_transacoes = st.number_input("Número de Transações", min_value=0)
pais_origem = st.selectbox("País de Origem", options=[0, 1])

# Criação do dataframe para previsão
dados_usuario = pd.DataFrame({
'valor_transacao': [valor_transacao],
'tempo_conta': [tempo_conta],
'num_transacoes': [num_transacoes],
'pais_origem': [pais_origem]
})

# Botão para previsão
if st.button("Analisar Transação"):
    resultado = fazer_previsao(dados_usuario)
    if resultado == 1:
        st.error("Transação suspeita! Possível fraude detectada.")
    else:
        st.success("Transação parece legítima.")