# Import des librairies
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Multimedia Diffusion - Vos séries", page_icon=":bar_chart:")

# Créer une mise en page en deux colonnes
col2, col1 = st.columns([5, 1])

# Afficher le logo dans la première colonne (à droite)
with col1:
    st.image('https://github.com/PikaChou82/Magma_Analytics/blob/main/Images/Multimedia.png?raw=true', width=100)

st.markdown("<h1 style='color:darkblue; font-family:Arial; font-size:50px;'>Bienvenue dans votre espace séries</h1>", unsafe_allow_html=True)

# Fond d'écran
image_url = "https://github.com/PikaChou82/Magma_Analytics/blob/main/Images/fond.jpg?raw=true"
st.markdown(f"""
<style>
.stApp {{
    background-image: url({image_url});
    background-size: cover;
    background-position: center center;
}}
</style>
""", unsafe_allow_html=True)

# Chargement et préparation des données
url_serie = "https://raw.githubusercontent.com/PikaChou82/Magma_Analytics/refs/heads/main/Datasets/df_definitif_series.csv"
url_reco = "https://raw.githubusercontent.com/PikaChou82/Magma_Analytics/refs/heads/main/Datasets/df_reco_series_final.csv"
base_image = "https://image.tmdb.org/t/p/w500/"
dataset = pd.read_csv(url_serie, sep=',', encoding='utf-8')
dataset_reco = pd.read_csv(url_reco, sep=',', encoding='utf-8')
liste_genres = dataset['genres'].unique()

# Initialisation des variables d'état
if 'afficher_bloc_series' not in st.session_state:
    st.session_state.afficher_bloc_series = True
if 'serie_selectionnee' not in st.session_state:
    st.session_state.serie_selectionnee = None
if 'parentTconst' not in st.session_state:
    st.session_state.parentTconst = None

# Fonction pour sélectionner une série
def select_serie(serie, parentTconst):
    st.session_state.serie_selectionnee = serie
    st.session_state.parentTconst = parentTconst
    st.session_state.afficher_bloc_series = False

# Fonction pour revenir à la liste des séries
def back():
    st.session_state.afficher_bloc_series = True
    st.session_state.serie_selectionnee = None
    st.session_state.parentTconst = None

# Bloc 1 : Affichage des séries
if st.session_state.afficher_bloc_series:
    genre = st.selectbox("Choisissez un genre", liste_genres)
    st.write("Vous avez choisi :", genre)

    dataset_filtre = dataset[dataset['genres'] == genre][['title_series', 'vote_average', 'startYear', 'poster_path', 'parentTconst']]
    dataset_filtre = dataset_filtre.drop_duplicates()
    dataset_filtre = dataset_filtre.sort_values(by='vote_average', ascending=False)
    dataset_filtre = dataset_filtre.rename(columns={'title_series': 'Titre de la série', 'vote_average': 'Note', 'startYear': 'Année', 'poster_path': 'Affiche', 'parentTconst': 'parentTconst'})

    # Affichage des séries
    nb_colonnes = 4
    cols = st.columns(nb_colonnes)
    for index, row in dataset_filtre.iterrows():
        col = cols[index % nb_colonnes]
        with col:
            st.markdown(f"{row['Titre de la série']}")
            st.write("**Année** :", row['Année'])
            st.write("**Note** :", row['Note'])
            st.image(base_image + str(row['Affiche']), width=100)

            # Bouton de sélection
            st.button(
                "Voir plus",
                key=f"{row['parentTconst']}_{index}",
                on_click=select_serie,
                args=(row['Titre de la série'], row['parentTconst'])
            )

# Bloc 2 : Affichage des détails de la série sélectionnée
if not st.session_state.afficher_bloc_series and st.session_state.serie_selectionnee:
    st.button("Back to series", on_click=back)

    # Mise en page des deux colonnes pour afficher les details de la serie selectionnée et les series récommandées
    col1, col2 = st.columns([3, 2])

    # Colonne de gauche affichera les détails de la série sélectionnée
    with col1:
        st.write(f"{st.session_state.serie_selectionnee}")

        details_serie = dataset[dataset['parentTconst'] == st.session_state.parentTconst]
        if not details_serie.empty:
            details_row = details_serie.iloc[0]
            st.image(base_image + str(details_row['poster_path']), width=300)
            st.write(f"**Année** : {details_row['startYear']}")
            st.write(f"**Note** : {details_row['vote_average']}")
            st.write(f"**Genre** : {details_row['genres']}")
            st.write(f"**Synopsis** : {details_row.get('overview', 'Synopsis indisponible.')}")

        # Affichage des détails des saisons et épisodes
        st.markdown("**Saisons et Épisodes**")

        def afficher_saison_episodes(series_id):
        
            episodes = dataset[dataset['parentTconst'] == series_id]
            if episodes.empty:
                st.write("Aucun détail disponible pour cette série.")
                return

            grouped = episodes.groupby('seasonNumber')
            # Menu déroulant pour choisir la saison souhaitée
            selection = st.selectbox("Choisissez une saison", grouped)

            # Filtre pour afficher les épisodes de la saison selectionnée
            episodes_saison = episodes[episodes['seasonNumber'] == selection].sort_values(by='episodeNumber')
        
            # Boucle pour afficher les épisodes 
            for index, episode in episodes_saison.iterrows():
                st.image(base_image + str(episode['poster_path']), width=150)
                st.write(f"{episode['title_episode']}")
                st.write(f"**Synopsis**: {episode['overview']}")
                

        afficher_saison_episodes(st.session_state.parentTconst)

    # Colonne de droite affichera les séries similaires recommandées
    with col2:
        st.markdown("### Séries similaires recommandées")

        # Filtre le dataset_reco pour trouver les recommandations de la série sélectionnée
        details_reco = dataset_reco[dataset_reco['parentTconst'] == st.session_state.parentTconst]

        if details_reco.empty:
            st.error("Je n'ai pas trouvé de recommandation pour cette série.")
        else:
            details_reco = details_reco.iloc[0]  # On récupère la première ligne des recommandations

            # Affichage des recommandations
            for voisin_col in ['voisin1', 'voisin2', 'voisin3', 'voisin4']:
                voisin_nom = details_reco[voisin_col]

                # Ignorer la série sélectionnée 
                if voisin_nom != st.session_state.serie_selectionnee:

                    # Vérification de l'existence d'un voisin
                    voisin_details = dataset_reco[dataset_reco['title_series'] == voisin_nom]

                    if not voisin_details.empty:
                        voisin_details_reco = voisin_details.iloc[0]
                        st.write(f"**{voisin_nom}**")
                        st.image(base_image + str(voisin_details_reco['poster_path']), width=100)
                        st.write(f"**Année** : {voisin_details_reco['startYear']}")
                        st.write(f"**Note** : {voisin_details_reco['vote_average']}")
                        st.write("---")
                    else:
                        st.warning(f"Pas d'infos pour cette série recommandée : {voisin_nom}")
