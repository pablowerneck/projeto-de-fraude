import streamlit as st
import pickle
import numpy as np

# Carregando o modelo
with open('modelo_fraude.pkl', 'rb') as file:
    fraud_model = pickle.load(file)


# Interface gráfica
st.title("Detecção de Fraude")
st.write("Este aplicativo detecta transações fraudulentas com base em dados históricos.")

#2- Capturando as informações de transação
# Campos para entrada de dados
valor_transacao = st.number_input("Valor da Transação (em dolares)", min_value=0, max_value=10000, value=50)
tempo_conta = st.number_input("Tempo da Conta (meses)", min_value=0, max_value=120, value=6)
num_transacoes_ult_30d = st.number_input("Número de Transações nos últimos 30 dias", min_value=0, max_value=1000, value=3)

# Para simplificar, vamos usar um selectbox para país de origem
pais_origem_opcoes={
    "Brasil": 0,
    "EUA": 1,
    "Outros": 2
}

pais_origem_escolhido=st.selectbox("País de Origem", list(pais_origem_opcoes.keys()))
pais_origem=pais_origem_opcoes[pais_origem_escolhido]

#3 Botão de Predição

if st.button("Verificar se é Fraude"):
    #constroi um array/reshape adequado para o modelo
    input_array=np.array([[valor_transacao, tempo_conta, num_transacoes_ult_30d, pais_origem]])

    #4 Executa a predição
    pred = fraud_model.predict(input_array)
    proba = fraud_model.predict_proba(input_array)

    st.write("## Resultado da Análise:")
    if pred[0]==1:
        st.error("Alerta: Transação com alto risco de Fraude.")
    else:
        st.success("Transação aparentemente legítima")

    #5 Probabilidade de fraude (opcional)
    st.write(f"** Probabilidade de Não Fraude:**{proba[0][0]:.2f}")
    st.write(f"** Probabilidade de Fraude:**{proba[0][1]:.2f}")

else:
    st.write ("Informe os detalhes e clique em 'Verificar se é Fraude'")
