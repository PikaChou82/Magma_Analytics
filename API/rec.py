import streamlit as st
import pandas as pd

# Titre et configuration
st.set_page_config(page_title="Multimedia Diffusion - Vos films", page_icon=":bar_chart:")

# Disposition de la page
col2, col1 = st.columns([5, 1])
with col1:
    # Logo
    st.image(f'https://github.com/PikaChou82/Magma_Analytics/blob/main/Images/Multimedia.png?raw=true', width=100)
with col2:
    st.title("Bienvenue dans votre espace de recherche")

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
url = "https://raw.githubusercontent.com/PikaChou82/Magma_Analytics/refs/heads/main/Datasets/movies_with_reco.csv"
url_actors = "https://raw.githubusercontent.com/PikaChou82/Magma_Analytics/refs/heads/main/Datasets/actors.csv"
base_image = "https://image.tmdb.org/t/p/w500/"
dataset = pd.read_csv(url, sep=',', encoding='utf-8')
dataset_actors = pd.read_csv(url_actors, sep=',', encoding='utf-8')
liste_genres = dataset['genres'].unique()

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
    # Sélection du genre
    genre = st.selectbox("Choisissez un genre", liste_genres)
    st.write("Vous avez choisi :", genre)
    
    # Nouveau champ pour le titre
    titre_recherche = st.text_input("Choisissez un titre", "")
    
    # Nouveau champ pour l'acteur
    acteur_recherche = st.text_input("Choisissez un acteur", "")
    
    # Nouveau champ pour l'année
    annee_recherche = st.text_input("Choisissez une année", "")

    # Filtrer les films selon le genre et le titre et acteur recherchés
    if genre:
        dataset_filtre = dataset[dataset['genres'] == genre]
    else:
        dataset_filtre = dataset  # Si aucun genre n'est sélectionné, ne pas filtrer

    # Filtrer par titre si un texte est entré
    if titre_recherche:
        dataset_filtre = dataset_filtre[dataset_filtre['title'].str.contains(titre_recherche, case=False, na=False)]
    
    # Filtrer par acteur si un texte est entré
    if acteur_recherche:
        dataset_filtre = dataset_filtre[dataset_filtre['actors'].str.contains(acteur_recherche, case=False, na=False)]
    
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

    st.button("Back to Films",on_click=back)

    st.write(f"### {st.session_state.film_selectionne}")
    row_film = dataset[dataset['imdb_id'] ==st.session_state.imdb_id].index[0]
    voisins = pd.DataFrame(dataset.loc[row_film, ['Voisin1', 'Voisin2', 'Voisin3', 'Voisin4']])
    propal = voisins.iloc[:,0].to_list()
    try : propal.remove(row_film)
    except : propal.pop()

    set_actors = pd.DataFrame(dataset_actors[dataset_actors['tconst'] == st.session_state.imdb_id])
    actor1= list(set_actors[set_actors['ordering']==1]['primaryName'].values)
    actor2= list(set_actors[set_actors['ordering']==2]['primaryName'].values)
    actor3= list(set_actors[set_actors['ordering']==3]['primaryName'].values)

    st.image(base_image + str(dataset.loc[row_film,'poster_path']), width=200)
    st.write("")
    st.write(f"**Année** : {dataset.loc[row_film,'startYear']} - **Recommandé à** {dataset.loc[row_film,'averageRating']*10} %")
    st.write(f"**Scenario**\n{dataset.loc[row_film,'overview']}")
    st.write("")

    actor1_name = actor1[0] if actor1 else "Unknown"
    actor2_name = actor2[0] if actor2 else "Unknown"
    actor3_name = actor3[0] if actor3 else "Unknown"
    if actor1_name != "Unknown" and actor2_name != "Unknown" and actor3_name != "Unknown":
        st.write(f"Avec {actor1_name}, {actor2_name} et {actor3_name}")
    elif actor1_name != "Unknown" and actor2_name != "Unknown" :
        st.write(f"Avec {actor1_name} et {actor2_name}")
    elif actor2_name != "Unknown" and actor3_name != "Unknown" :
        st.write(f"Avec {actor2_name} et {actor3_name}")    
    elif actor1_name != "Unknown" and actor3_name != "Unknown" :
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
