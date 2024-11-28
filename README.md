# Magma_Analytics
Projet Multimédia Diffusion / Magma Analytics - WCS

# Etapes :
## Sélection des Tables finales
  Table 1960_85+ [AUDREY]
  Filtre : +85 minutes / films diffusés sur la région France / sortis après 1960
  KPIs : 
      Nombre total de films ok
      Nombre de films par année de sortie ok
      Durée moyenne des films ok
      Nombre de films par genre ok
      Top 10 des films les mieux notés ok
  Statut : Ok
  
  Table acteurs [MARIAMMA]
  Filtre : films disponibles dans la table 1960_85+
  KPIs : 
    Nombre moyen d'acteurs par film (seulement pour le top10)
    Répartition des acteurs par genre de films : Pourcentage ou nombre absolu d'acteurs dans chaque genre de films.
    Top 10 des acteurs les plus actifs : Les acteurs ayant joué dans le plus grand nombre de films
    Nombre total d'acteurs
    Nombre de films par acteur par genre : Nombre de films par acteur, ventilé par genre, pour voir les préférences de genre des acteurs.
  Statut : en cours
  
Table TMDB [MEDHI]
  Filtre : films disponibles dans la table 1960_85+
  KPIs :
    Budget
    Revenus
    Compagnies de production
    Pays de production
  Champs importants : 
      url
      imdb_id
      overview
      popularity
      poster_path
      spoken_langages
      video
  Statut : en cours

  Table série [AMADOU]
  Filtre : à définir
  KPIs : 
      Nombre total de séries 
      Nombre de séries par année de sortie 
      Nombre de séries par genre 
      Top 10 des séries les mieux notées
  Statut : en cours

  Table Title Principals [ALL]
    Filtre : films disponibles dans la table 1960_85+
    Méthode : On chunke TITLE_PRINCIPALS en tranche de 6 000 000
        Giulio = 0 à 18 000 000
        Mariamma = 18 000 001 à 36 000 000
        Medhi = 36 000 001 à 54 000 000
        Audrey = 54 000 0001 à 72 000 000
        Amadou = 72 000 0001 à 90 000 0000
        Chacun filtre son dataset puis on concatène

## KPIS [ALL]
  Fichier Power_BI Projet2_KPIs
  Statut : Ok sur films, en attente série et Tmdb

## API [ALL]
  Dossier API
  1 Page principale où on choisit une page films / une page série / une page recherche ?
    A faire : proposer la page recheche [AUDREY]
              proposer une sélection de ses préférences utilisateurs (création dictionnaire puis affichage de ses infos et préférences)
  1 Page films
    A faire : améliorer le visuel
              rajouter un choix de sélection pour aller sur une page choix
  1 Page série : améliorer le visuel
              rajouter un choix de sélection pour aller sur une page choix
  1 Page recherche : [GIULIO]
    A créer avec plusieurs possibilités de critères
  1 Page sélection : [AUDREY]
    A créer avec toutes les infos du film (nom, date, producteur, acteurs, overview, bande annonce, affiche)
    Ajouter une modèle ML de classification
  
