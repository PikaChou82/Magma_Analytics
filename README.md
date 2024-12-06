# Magma_Analytics
Projet Multimédia Diffusion / Magma Analytics - WCS

# Etapes :
## Sélection des Tables finales
  **Movies Final [AUDREY & MEDHI]**
  
  Filtre : +85 minutes / films diffusés sur la région France / sortis après 1960 / note supérieure à 6
  
  KPIs : <br>
      Nombre total de films ok <br>
      Nombre de films par année de sortie ok <br>
      Durée moyenne des films ok <br>
      Nombre de films par genre ok <br>
      Top 10 des films les mieux notés ok <br>
  **Statut : Ok**
  
  **Table acteurs [MARIAMMA]**
  
  Filtre : films disponibles dans la table 1960_85+
  
  KPIs :  <br>
    Nombre moyen d'acteurs par film (seulement pour le top10) <br>
    Répartition des acteurs par genre de films : Pourcentage ou nombre absolu d'acteurs dans chaque genre de films. <br>
    Top 10 des acteurs les plus actifs : Les acteurs ayant joué dans le plus grand nombre de films <br>
    Nombre total d'acteurs <br>
    Nombre de films par acteur par genre : Nombre de films par acteur, ventilé par genre, pour voir les préférences de genre des acteurs. <br>
  **Statut : en cours**
  
**Table TMDB [MEDHI]**
  
  Filtre : films disponibles dans la table 1960_85+
  
  KPIs : <br>
    Budget <br>
    Revenus <br>
    Compagnies de production <br>
    Pays de production <br>
  Champs importants :  <br>
      url <br>
      imdb_id <br>
      overview <br>
      popularity <br>
      poster_path <br>
      spoken_langages <br>
      video <br>
  **Statut : en cours**

  **Table série [AMADOU & MEDHI]**
  
  Filtre : à partir de 1960
  
  KPIs :  <br>
      Nombre total de séries  <br>
      Nombre de séries par année de sortie  <br>
      Nombre de séries par genre  <br>
      Top 10 des séries les mieux notées <br>
  **Statut : en cours**

  **Table Title Principals [ALL]**
  
    Filtre : films disponibles dans la table 1960_85+
    
    Méthode : On chunke TITLE_PRINCIPALS en tranche de 6 000 000 <br>
        Giulio = 0 à 18 000 000 <br>
        Mariamma = 18 000 001 à 36 000 000 <br>
        Medhi = 36 000 001 à 54 000 000 <br>
        Audrey = 54 000 0001 à 72 000 000 <br>
        Amadou = 72 000 0001 à 90 000 0000 <br>
        Chacun filtre son dataset puis on concatène <br>

## KPIS [ALL]
  Fichier Power_BI Projet2_KPIs <br>
  **Statut : Ok sur films, en attente série et Tmdb**

## API [ALL]

  Dossier API
  
  1 Page principale où on choisit une page films / une page série / une page recherche [AUDREY] <br>
    Créée avec les infos utilisateurs <br>
  1 Page films <br>
    A faire : améliorer le visuel
              rajouter un choix de sélection pour aller sur une page choix <br>
  1 Page série : améliorer le visuel <br>
              rajouter un choix de sélection pour aller sur une page choix <br>
  1 Page recherche : [GIULIO & MARIAMMA] <br>
    A créer avec plusieurs possibilités de critères <br>
  1 Page sélection : [AUDREY] <br>
    Créée avec toutes les infos du film (nom, date, acteurs, overview, affiche)
    Modèle de Classification (Nearest Neighbours)
  
