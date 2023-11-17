import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Pontos de coleta de resíduos sólidos",
    page_icon="♻️",
)

df_dados = st.session_state["dados"]

st.title('🗺️ Endereço dos pontos de coleta ')
st.markdown("")
st.markdown('''Para encontrar uma ecoestção perto de você, selecione nos menus do lado esquerdo a região do Recife ou região metropolitana que você mora e em seguida o bairro. Abaixo aparecerá que tipo de 
            material é coletado, endereço e qual organização coleta.''')
st.markdown("")

regioes = df_dados['regiao'].value_counts().index
regiao = st.sidebar.selectbox("Região", regioes)

df_bairros = df_dados[df_dados['regiao'] == regiao]
bairros = df_bairros['bairro'].value_counts().index
bairro = st.sidebar.selectbox("Bairros", bairros)

mostra_bairro = df_dados[df_dados["bairro"] == bairro]

colunas = ['tiporesiduo',"endereco","complemento","observacao"]
st.dataframe(mostra_bairro[colunas], hide_index=True)