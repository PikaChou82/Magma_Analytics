
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

st.markdown("<h1 style='color:darkblue; font-family:Arial; font-size:30px;'>Bienvenue dans votre espace Multimédia</h1>", unsafe_allow_html=True)
st.write("")

video_url = 'https://raw.githubusercontent.com/PikaChou82/Magma_Analytics/main/Images/générique-médiavision-jean-mineur.mp4'
st.video(video_url)

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
        "type1": "films",
        "type2": "séries",
        "langue": "fr",
        "genre1": "action",
        "genre2" : "aventure",
        "genre3" : "fantastique"
    }
}

utilisateur2 = {
        "id" : "pascalejamot",
       "nom": "Jamot",
    "prenom": "Pascale",
    "email": "pascale.jamot@neuf.fr",
    "preferences": {
        "type1": "films",
        "type2": "séries",
        "langue": "fr",
        "genre1": "action",
        "genre2" : "biography",
        "genre3" : "comedy"
    }
}

utilisateurs = [utilisateur1['id'],utilisateur2['id']]

# Rentrer un nom d'utilisateur pour accéder à sa page personnalisée

st.markdown("""
<style>
.stTextInput input {
  background-color: 'darkgrey';  /* Couleur de fond */
  color: 'darkblue';               /* Couleur du texte */
  border: 2px solid #007bff;  /* Bordure */
}
.stTextInput label {
  color: 'darkblue';  /* Couleur du texte du label */
</style>
            
""", unsafe_allow_html=True)

user = st.text_input("Veuillez vous identifier pour plonger dans **votre** monde du cinéma ", value="Votre nom ici")

# Bouton de validation
if st.button("Me connecter"):
    # Si le bouton est cliqué, on affiche un message de confirmation
    if user in utilisateurs :
        user = utilisateurs.index(user)
        user = [utilisateur1, utilisateur2][user]
        st.write(f"###  Bonjour {user['prenom']} !")
        st.write("Ravis de vous revoir, et bienvenue dans votre espace.")
        st.write("")
        st.write(f"#### Vos genres préférés : **{user['preferences']['genre1']}**, **{user['preferences']['genre2']}** et **{user['preferences']['genre3']}**")
        st.write("")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('[Aller voir les films](https://magmaanalytics-filmspage.streamlit.app/)', unsafe_allow_html=True)
        with col2:
            st.markdown('[Aller voir les séries](https://magmaanalytics-seriespage.streamlit.app/)', unsafe_allow_html=True)
        with col3:
            st.markdown('[Recherche avancée](https://magmaanalytics-recherchepage.streamlit.app/)', unsafe_allow_html=True)

            
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
