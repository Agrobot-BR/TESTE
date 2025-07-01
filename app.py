
import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Agrobot - Previsão de Umidade", layout="centered")
st.title('🌱 Agrobot - Previsão de Umidade do Solo')

# Carregar modelo
try:
    model = joblib.load('modelo_umidade_compat.pkl')
except Exception as e:
    st.error(f"Erro ao carregar o modelo: {e}")

# Inputs do usuário
umidade_atual = st.slider('Umidade Atual do Solo (%)', 0.0, 100.0, 50.0, step=0.1)
temperatura = st.slider('Temperatura (°C)', 0.0, 50.0, 25.0, step=0.1)
pH = st.slider('pH do Solo', 3.0, 9.0, 6.5, step=0.1)
EC = st.number_input('Condutividade Elétrica (µS/cm)', min_value=0.0, max_value=3000.0, value=500.0, step=1.0)
N = st.number_input('Nitrogênio (mg/kg)', min_value=0.0, max_value=100.0, value=20.0, step=1.0)
P = st.number_input('Fósforo (mg/kg)', min_value=0.0, max_value=100.0, value=15.0, step=1.0)
K = st.number_input('Potássio (mg/kg)', min_value=0.0, max_value=200.0, value=30.0, step=1.0)

# Botão de Previsão
if st.button('🔍 Prever Umidade Futura'):
    entrada = np.array([[umidade_atual, temperatura, pH, EC, N, P, K]])
    try:
        resultado = model.predict(entrada)
        st.success(f'🌿 Previsão de Umidade nas próximas 24 horas: **{resultado[0]:.2f}%**')
    except Exception as e:
        st.error(f"Erro na previsão: {e}")
