# Import des librairies
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import subprocess
from PIL import Image

# Titre
st.set_page_config(page_title="Multimedia Diffusion", page_icon=":bar_chart:")

# Créer une mise en page en deux colonnes
col2, col1 = st.columns([5, 1])

# Afficher le logo dans la première colonne (à droite)
with col1:
    st.image(f'https://github.com/PikaChou82/Magma_Analytics/blob/main/Images/Multimedia.png?raw=true', width=100)

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

def ouvrir_application(chemin):
    if st.session_state.get('os') == 'Windows':
        subprocess.Popen(f'start {chemin}', shell=True)
    elif st.session_state.get('os') == 'Linux':
        subprocess.Popen(f'xdg-open {chemin}', shell=True)
    elif st.session_state.get('os') == 'Darwin':  # macOS
        subprocess.Popen(['open', chemin])

st.button('Aller aux films', on_click=lambda: ouvrir_application('films.py'))
st.button('Aller aux séries', on_click=lambda: ouvrir_application('series.py'))

# Détecter le système d'exploitation (à exécuter une seule fois)
if 'os' not in st.session_state:
    import platform
    st.session_state.os = platform.system()
