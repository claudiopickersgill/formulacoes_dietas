import streamlit as st
from pages.principal import principal
from pages.calcular_dieta import calcular_dieta
from pages.carregar_dieta import carregar_dieta
from pages.adicionar_ingrediente import adicionar_ingrediente

# Menu lateral
st.sidebar.title("Menu")
menu = st.sidebar.selectbox('Selecione uma Página', [
    'Principal', 'Calcular Dieta', 'Carregar Dieta', 'Adicionar Ingrediente'])

if menu == 'Principal':
     principal.principal()
elif menu == 'Calcular Dieta':
    calcular_dieta.calcular_dieta()
elif menu == 'Carregar Dieta':
    carregar_dieta.carregar_dieta()
elif menu == 'Adicionar Ingrediente':
    adicionar_ingrediente.adicionar_ingrediente()
