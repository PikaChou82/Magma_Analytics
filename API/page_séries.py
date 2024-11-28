# Import des librairies
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from PIL import Image

st.set_page_config(page_title="Multimedia Diffusion - Vos séries", page_icon=":bar_chart:")

# Créer une mise en page en deux colonnes
col2, col1 = st.columns([5, 1])

# Afficher le logo dans la première colonne (à droite)
with col1:
    st.image(f'https://github.com/PikaChou82/Magma_Analytics/blob/main/Images/Multimedia.png?raw=true', width=100)

st.markdown("<h1 style='color:darkblue; font-family:Arial; font-size:50px;'>Bienvenue dans votre espace séries</h1>", unsafe_allow_html=True)
st.write("")
st.write("")

# Fond d'écran
image_url = "https://github.com/PikaChou82/Magma_Analytics/blob/main/Images/fond.jpg?raw=true"

st.markdown(r"""
<style>
.stApp {
    background-image: url(""" + image_url + """);
    background-size: cover;
    background-position: center center;
}
</style>
""", unsafe_allow_html=True)

genre = st.selectbox("Choisissez un genre", ["Action", "Comédie", "Science-fiction"])
st.write("Vous avez choisi :", genre)
