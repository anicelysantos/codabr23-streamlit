#importa as bibliotecas
import streamlit as st
import pandas as pd
import webbrowser

#Configura detalhes da página
st.set_page_config(
    page_title="Início",
    page_icon="♻️",
)

#Carrega a base de dados direto do GitHub
DATA_URL = ('https://raw.githubusercontent.com/anicelysantos/codabr23-streamlit/main/pontos-coleta-recife.csv')

#Carrega a base de dados acima em uma variável para usar dentro do código
dados = pd.read_csv(DATA_URL)

#Constrói um "cache" dos dados
st.session_state["dados"] = dados


st.title('Pontos de coleta em Recife')

st.markdown(''' ### O Lixo é responsabilidade de todos''')
st.markdown('''Você já parou para pensar o que acontece com o lixo que sai da sua casa? E que o futuro desse material 
            depende muito da sua atitude? Quando o cidadão encaminha o lixo para a reciclagem, além de evitar mais acúmulo 
            de material nos aterros, garante que menos recursos naturais sejam extraídos para a fabricação de outros produtos e 
            contribui para a geração de emprego e renda de muitos trabalhadores¹.''') 
            
st.markdown('O gráfico abaixo mostra a quantidade de pontos de coleta por região.')

#Sumariza as regiões
qt_regiao = dados['regiao'].value_counts()

#Mostra a sumarização em um gráfico
st.bar_chart(data=qt_regiao)


st.markdown(''' As ecoestações são pontos de recebimento de resíduos, cujo objetivo é oferecer uma alternativa à população para o descarte de móveis velhos, resíduos de pequenas obras residenciais e outros materiais, com volume de até 1m3/dia. Resíduos hospitalares, lixo industrial e equipamentos eletroeletrônicos não são recebidos nas EcoEstações. O horário de funcionamento é das 8:00h as 16:00h, de segunda a sábado, exceto feriados.²

Os econúcleos são núcleos de educação ambiental, em funcionamento desde 2013. Confira abaixo onde estão localizadas as ecoestações no Recife e região metropolita.''')    

#Transforma os dados de localização em float
dados['lat'] = dados['lat'].astype(float)
dados['lon'] = dados['lon'].astype(float)

#Constrói um mapa com os dados
st.map(dados)     

st.markdown('''Clique no botão abaixo caso deseje ter acesso aos dados brutos, limpos e ao script to projeto.''')  


#Botões na sidebar organizado em colunas
col1,col2,col3 = st.columns(3)

btn1 = col1.button('Dados da prefeitura do Recife')
if btn1:
    webbrowser.open_new_tab("http://dados.recife.pe.gov.br/dataset/destinacao-de-residuos-solidos")

btn2 = col2.button('Dados limpos')
if btn2:
    webbrowser.open_new_tab("https://github.com/anicelysantos/codabr23-streamlit/blob/main/pontos-coleta-recife.csv")

btn3 = col3.button('Projeto')
if btn3:
    webbrowser.open_new_tab("https://github.com/anicelysantos/codabr23-streamlit/tree/main")

st.markdown('')            
st.markdown('''¹ [https://especiais.ne10.uol.com.br/coleta-seletiva/](https://especiais.ne10.uol.com.br/coleta-seletiva/)''')
st.markdown('''² [http://dados.recife.pe.gov.br/dataset/destinacao-de-residuos-solidos](http://dados.recife.pe.gov.br/dataset/destinacao-de-residuos-solidos)''')

st.sidebar.markdown('Desevolvido por Anicely Santos para o [Coda.Br 2023](https://escoladedados.org/coda/coda2023/)')