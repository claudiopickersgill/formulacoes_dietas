import streamlit as st
from pages.principal import principal

# Menu lateral
st.sidebar.title("Menu")
menu = st.sidebar.selectbox('Selecione uma Página', [
    'Principal', 'Calcular Dieta', 'Carregar Dieta', 'Adicionar Ingrediente'])

if menu == 'Principal':
     principal.principal()
# elif menu == 'Calcular ODDS':
#     odds.odds()
# elif menu == 'Adicionar Jogo na Base':
#     add_jogo.interface()
# elif menu == 'Gráficos':
#     graficos.graficos()
