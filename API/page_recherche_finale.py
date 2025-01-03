import streamlit as st
import pandas as pd

# Titre et configuration
st.set_page_config(page_title="Multimedia Diffusion - Recherche avancée", page_icon=":bar_chart:")

# Disposition de la page
col2, col1 = st.columns([5, 1])
with col1:
    # Logo
    st.image(f'https://github.com/PikaChou82/Magma_Analytics/blob/main/Images/Multimedia.png?raw=true', width=100)
with col2:
    st.markdown("<h1 style='color:darkblue; font-family:Arial; font-size:40px;'>Bienvenue dans votre espace recherche</h1>", unsafe_allow_html=True)
    st.write("")
    st.write("")

# Fond d'écran
image_url = "https://github.com/PikaChou82/Magma_Analytics/blob/main/Images/fond.jpg?raw=true"
st.markdown(f"""
<style>
.stApp {{
    background-image: url('{image_url}');
    background-size: cover;
    background-position: center center;
}}
</style>
""", unsafe_allow_html=True)

# Chargement et préparation des données
url = "https://raw.githubusercontent.com/PikaChou82/Magma_Analytics/refs/heads/main/Datasets/movies_with_reco_actors.csv"
url2 = "https://raw.githubusercontent.com/PikaChou82/Magma_Analytics/refs/heads/main/Datasets/actors.csv"
url3 = "https://raw.githubusercontent.com/PikaChou82/Magma_Analytics/refs/heads/main/Datasets/df_definitif_series.csv"
base_image = "https://image.tmdb.org/t/p/w500/"
dataset_actors = pd.read_csv(url2, sep=',', encoding='utf-8')
dataset = pd.read_csv(url, sep=',', encoding='utf-8')
series = pd.read_csv(url3, sep=',', encoding='utf-8')

liste_genres = ["Tous les genres"] + list(dataset['genres'].unique())
liste_genres_series = ["Tous les genres"] + list(series['genres'].unique())
liste_type = ['Film', 'Série']

#                               ***FILMS***
#******************************************************************************
# Initialisation des variables d'état pour l'affichage des différents blocs
if 'afficher_bloc_films' not in st.session_state:
    st.session_state.afficher_bloc_films = True
if 'film_selectionne' not in st.session_state:
    st.session_state.film_selectionne = None
if 'imdb_id' not in st.session_state:
    st.session_state.imdb_id = None



# Création d'une fonction pour sélectionner un film et forcer les états de blocs
def select_film(film, imdb_id):
    st.session_state.film_selectionne = film
    st.session_state.imdb_id = imdb_id
    st.session_state.afficher_bloc_films = False


def back():
    st.session_state.afficher_bloc_films = True

# Bloc 1 : Affichage des films

if st.session_state.afficher_bloc_films:

    # Choix du type film ou série
    type = st.selectbox("Choisissez un type", liste_type)
    st.write("Vous avez choisi :", type)
    st.write("")

    # Sélection du genre avec "Tous les genres" comme valeur par défaut
    genre = st.selectbox("Choisissez un genre", liste_genres, index=0)
    st.write("Vous avez choisi :", genre)
    st.write("")

    # Nouveau champ pour le titre
    titre_recherche = st.text_input("Choisissez un titre", "")
    
    # Nouveau champ pour l'acteur
    acteur_recherche = st.text_input("Choisissez un acteur", "")
    
    # Nouveau champ pour l'année
    annee_recherche = st.text_input("Choisissez une année", "")

    # Filtrer les films selon le genre, le titre, l'acteur, et l'année
    if type == "Film":
        if genre and genre != "Tous les genres":
            dataset_filtre = dataset[dataset['genres'] == genre]
        else:
            dataset_filtre = dataset  # Si "Tous les genres" est sélectionné, ne pas filtrer

        # Filtrer par titre si un texte est entré
        if titre_recherche:
            dataset_filtre = dataset_filtre[dataset_filtre['title'].str.contains(titre_recherche, case=False, na=False)]
        
        # Filtrer par acteur si un texte est entré
        if acteur_recherche:
            dataset_filtre = dataset_filtre[dataset_filtre['primaryName'].str.contains(acteur_recherche, case=True, na=False)]
        
        # Filtrer par année si un texte est entré
        if annee_recherche:
            dataset_filtre = dataset_filtre[dataset_filtre['startYear'].astype(str).str.contains(annee_recherche)]

        dataset_filtre = dataset_filtre.loc[:, ['title', 'averageRating', 'startYear', 'poster_path', 'imdb_id']]
        dataset_filtre = dataset_filtre.sort_values(by='averageRating', ascending=False)
        dataset_filtre = dataset_filtre.rename(columns={'title': 'Titre du film', 'averageRating': 'Note', 'startYear': 'Année', 'poster_path': 'Affiche', 'imdb_id': 'imdb_id'})

        # Affichage des films
        nb_colonnes = 4
        cols = st.columns(nb_colonnes)
        for index, row in dataset_filtre.iterrows():
            col = cols[index % nb_colonnes]
            with col:
                st.markdown(f"**{row['Titre du film']}**")
                st.write("Année :", row['Année'])
                st.write("Note :", row['Note'])
                st.image(base_image + str(row['Affiche']), width=100)
                
                # Bouton de sélection
                st.button(
                    "Voir plus",
                    key=row['imdb_id'],
                    on_click=select_film,
                    args=(row['Titre du film'], row['imdb_id']) 
                )

# Bloc 2 : Détails du film sélectionné

if not st.session_state.afficher_bloc_films and st.session_state.film_selectionne:

    st.button("Back to Search", on_click=back)

    st.write(f"### {st.session_state.film_selectionne}")
    row_film = dataset[dataset['imdb_id'] == st.session_state.imdb_id].index[0]
    voisins = pd.DataFrame(dataset.loc[row_film, ['Voisin1', 'Voisin2', 'Voisin3', 'Voisin4']])
    propal = voisins.iloc[:, 0].to_list()
    try:
        propal.remove(row_film)
    except:
        propal.pop()

    set_actors = pd.DataFrame(dataset_actors[dataset_actors['tconst'] == st.session_state.imdb_id])
    actor1 = list(set_actors[set_actors['ordering'] == 1]['primaryName'].values)
    actor2 = list(set_actors[set_actors['ordering'] == 2]['primaryName'].values)
    actor3 = list(set_actors[set_actors['ordering'] == 3]['primaryName'].values)

    st.image(base_image + str(dataset.loc[row_film, 'poster_path']), width=200)
    st.write("")
    st.write(f"**Année** : {dataset.loc[row_film,'startYear']} - **Recommandé à** {dataset.loc[row_film,'averageRating']*10} %")
    st.write(f"**Genre** : {dataset.loc[row_film,'genres']}")
    st.write(f"**Scenario**\n{dataset.loc[row_film,'overview']}")
    st.write("")

    actor1_name = actor1[0] if actor1 else "Unknown"
    actor2_name = actor2[0] if actor2 else "Unknown"
    actor3_name = actor3[0] if actor3 else "Unknown"
    if actor1_name != "Unknown" and actor2_name != "Unknown" and actor3_name != "Unknown":
        st.write(f"Avec {actor1_name}, {actor2_name} et {actor3_name}")
    elif actor1_name != "Unknown" and actor2_name != "Unknown":
        st.write(f"Avec {actor1_name} et {actor2_name}")
    elif actor2_name != "Unknown" and actor3_name != "Unknown":
        st.write(f"Avec {actor2_name} et {actor3_name}")    
    elif actor1_name != "Unknown" and actor3_name != "Unknown":
        st.write(f"Avec {actor1_name} et {actor3_name}")    

    st.write("Vous pourriez aussi aimer :")
    colonnes = st.columns(3)
    for i in range(len(propal)):
        with colonnes[i]:
            st.markdown(f"**{dataset.loc[propal[i],'title']}**")
            st.write("Année :", dataset.loc[propal[i],'startYear'])
            st.write("Note :", dataset.loc[propal[i],'averageRating'])
            st.image(base_image + str(dataset.loc[propal[i],'poster_path']), width=100)
            
            # Bouton de sélection
            st.button(
                "Voir plus",
                key=dataset.loc[propal[i],'imdb_id'],
                on_click=select_film,
                args=(dataset.loc[propal[i],'title'], dataset.loc[propal[i],'imdb_id']) 
            )

    
#                               ***SERIES***
#******************************************************************************

# Initialisation des variables d'état pour l'affichage des différents blocs
if 'afficher_bloc_series' not in st.session_state:
    st.session_state.afficher_bloc_series = True
if 'serie_selectionnee' not in st.session_state:
    st.session_state.serie_selectionnee = None
if 'parentTconst' not in st.session_state:
    st.session_state.parentTconst = None

# Création d'une fonction pour sélectionner une série et forcer les états de blocs
def select_serie(serie, parentTconst):
    st.session_state.serie_selectionnee = serie
    st.session_state.parentTconst = parentTconst
    st.session_state.afficher_bloc_series = False
    st.session_state.afficher_bloc_films = False
    st.session_state.film_selectionne = False


def back():
    st.session_state.afficher_bloc_films = True
    st.session_state.afficher_bloc_series = True
    st.session_state.serie_selectionnee = None
    st.session_state.parentTconst = None


# Bloc 1 : Affichage des series
if st.session_state.afficher_bloc_series:

    if type == "Série":
        if genre and genre != "Tous les genres":
            series_filtre = series[series['genres'] == genre]
        else:
            series_filtre = series  # Si "Tous les genres" est sélectionné, ne pas filtrer

        # Filtrer par titre si un texte est entré
        if titre_recherche:
            series_filtre = series_filtre[series_filtre['title_series'].str.contains(titre_recherche, case=False, na=False)]
        
        # Filtrer par acteur si un texte est entré
        #if acteur_recherche2:
        #    series_filtre = series_filtre[series_filtre['primaryName'].str.contains(acteur_recherche2, case=False, na=False)]
        
        # Filtrer par année si un texte est entré
        if annee_recherche:
            series_filtre = series_filtre[series_filtre['startYear'].astype(str).str.contains(annee_recherche)]

        series_filtre = series_filtre.loc[:, ['title_series', 'vote_average', 'startYear', 'poster_path', 'parentTconst']]
        series_filtre = series_filtre.drop_duplicates('parentTconst')
        series_filtre = series_filtre.sort_values(by='vote_average', ascending=False)
        series_filtre = series_filtre.rename(columns={'title_series': 'Titre de la série', 'vote_average': 'Note', 'startYear': 'Année', 'poster_path': 'Affiche', 'parentTconst': 'parentTconst'})


        # Affichage des séries
        nb_colonnes = 4
        cols = st.columns(nb_colonnes)
        for index, row in series_filtre.iterrows():
            col = cols[index % nb_colonnes]
            with col:
                st.markdown(f"**{row['Titre de la série']}**")
                st.write("Année :", row['Année'])
                st.write("Note :", row['Note'])
                st.image(base_image + str(row['Affiche']), width=100)
                
                # Bouton de sélection
                st.button(
                    "Voir plus",
                    key=row['parentTconst'],
                    on_click=select_serie,
                    args=(row['Titre de la série'], row['parentTconst']) 
                )

# Bloc 2 : Affichage des détails de la série sélectionnée
if not st.session_state.afficher_bloc_series and st.session_state.serie_selectionnee:
    st.button("Back to search", on_click=back)

    # Mise en page des deux colonnes pour afficher les details de la serie selectionnée et les series récommandées
    col1, col2 = st.columns([3, 2])

    # Colonne de gauche affichera les détails de la série sélectionnée
    with col1:
        st.write(f"{st.session_state.serie_selectionnee}")

        details_serie = series[series['parentTconst'] == st.session_state.parentTconst]
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
        
            episodes = series[series['parentTconst'] == series_id]
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
                

        afficher_saison_episodes(st.session_state.parentTconst)

    # Colonne de droite affichera les séries similaires recommandées
    with col2:

        st.markdown("### Séries similaires recommandées")