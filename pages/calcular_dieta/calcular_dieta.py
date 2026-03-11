import streamlit as st
import pandas as pd
from pages.conexao import cria_df
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_style(rc={'axes.facecolor': '#0E1117',
                  'axes.edgecolor': 'white',
                  'axes.labelcolor': 'white',
                  'text.color': 'white',
                  'xtick.color': 'white',
                  'ytick.color': 'white',
                  'axes.grid': True,
                  'grid.color': '.6',
                  "grid.linestyle": ":"})
fundo = '#0E1117'
loc = 'upper right'

def calcular_dieta():
    df = cria_df.cria_df()

    st.write(df.head())