# Magma_Analytics
Projet Multimédia Diffusion / Magma Analytics - WCS

## Membres :
Mariamma, Amadaou, Giulio, Mehdi et Audrey

## Etapes :

###  Sélection des tables

> [!NOTE]
> 1 Table movies_final regroupant la base Tmdb ainsi que la base Title_akas.
 Filtres appliqués : 
> - [X] +85 minutes
> - [X] Films diffusés sur la région France
> - [X] Films sortis après 1960
> - [X] Films dont la note est supérieure à 6
> - [X] Sample de 5 000 films

> [!TIP]
> Méthode de classification : KNearestNeighbors [3 proches voisins]
> Features retenues : ['isAdult','genres_','autre_prod_countries', 'directors', 'actor1_','actor2_','actor3_']]
> Process : RobustScaler puis PCA

> [!NOTE]
> 1 Table series_final regroupant la base Tmdb ainsi que la base Title_episodes.
 Filtres appliqués : 
> +85 minutes
> - [X] Films diffusés sur la région France
> - [X] Films sortis après 1960
> - [X] Films dont la note est supérieure à 6
> - [X] Sample de 200 séries

###  Sélection des KPI's

> [!NOTE]
> KPIs : <br>
> - [X] Films
> - [X] Acteurs
> - [ ] Séries
> - [ ] Tmdb

> [!IMPORTANT]
>  **KPIs restants TmdB**<br>
>  Budget <br>
>  Revenus <br>
>  Compagnies de production <br>
>  Pays de production <br>
>  **KPIs restants Séries**<br>
>  Nombre total de séries  <br>
>  Nombre de séries par année de sortie  <br>
>  Nombre de séries par genre  <br>
>  Top 10 des séries les mieux notées <br>

### API
  
1. 1 Page principale
   - On choisit une page films / une page série / une page recherche <br>

2. 1 Page films
   
3.  1 Page série
    
4. 1 Page recherche 
 
5. 1 Page sélection 
