# Import des librairies
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import subprocess
from PIL import Image

# Titre
st.set_page_config(page_title="Multimedia Diffusion", page_icon=":bar_chart:")

st.markdown("""
<style>
button {
  width: 400px;
  height: 50px;
  font-size: 18px;
  background-color: #4CAF50; /* Vert */
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  margin: 4px 2px;
  cursor: pointer;   

}
</style>
""", unsafe_allow_html=True)

# Créer une mise en page en deux colonnes
col2, col1 = st.columns([5, 1])

# Afficher le logo dans la première colonne (à droite)
with col1:
    st.image(f'https://github.com/PikaChou82/Magma_Analytics/blob/main/Images/Multimedia.png?raw=true', width=100)

st.markdown("<h1 style='color:darkblue; font-family:Arial; font-size:50px;'>Bienvenue dans votre espace Multimédia</h1>", unsafe_allow_html=True)
st.write("")
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

# Dictionnaire des users
utilisateur1 = {
    "id" : "karimadupont",
    "nom": "Dupont",
    "prenom": "Karima",
    "email": "karima.dupont@multimedia-diffusion.com",
    "preferences": {
        "type": "films",
        "langue": "fr",
        "genre": "action"
    }
}

utilisateur2 = {
        "id" : "pascalejamot",
       "nom": "Jamot",
    "prenom": "Pascale",
    "email": "pascale.jamot@neuf.fr",
    "preferences": {
        "type": "films",
        "langue": "fr",
        "genre": "comédie"
    }
}

utilisateurs = [utilisateur1['id'],utilisateur2['id']]

# Rentrer un nom d'utilisateur pour accéder à sa page personnalisée
user = st.text_input("Veuillez vous identifier pour plonger dans **votre** monde du cinéma ;)")

# Bouton de validation
if st.button("Me connecter"):
    # Si le bouton est cliqué, on affiche un message de confirmation
    if user in utilisateurs :
        user = utilisateurs.index(user)
        user = [utilisateur1, utilisateur2][user]
        st.write(f"Bonjour {user["prenom"]} ! Bienvenue dans votre espace :)")
        st.write("")
        st.write(f"Envie d'un {user['preferences']['type']} style {user["preferences"]["genre"]} ou on change ?")
        col1, col2 = st.columns(2)
        with col1:
            st.button('Go pour mes preferences', on_click=lambda: ouvrir_application('films.py'))
        with col2:
            st.button('Envie de changement', on_click=lambda: ouvrir_application('series.py'))
            
    else:
        st.write(f"désolé, je n'ai pas le plaisir de vous connaître... Rdv en cinéma pour vous inscrire avec notre équipe !")

# Détecter le système d'exploitation
if 'os' not in st.session_state:
    import platform
    st.session_state.os = platform.system()

def ouvrir_application(chemin):
    if st.session_state.get('os') == 'Windows':
        subprocess.Popen(f'start {chemin}', shell=True)
    elif st.session_state.get('os') == 'Linux':
        subprocess.Popen(f'xdg-open {chemin}', shell=True)
    elif st.session_state.get('os') == 'Darwin':  # macOS
        subprocess.Popen(['open', chemin])

col1, col2 = st.columns(2)
with col1:
    st.button('Rechercher un film', on_click=lambda: ouvrir_application('films.py'))
with col2:
    st.button('Rechercher une série', on_click=lambda: ouvrir_application('series.py'))
