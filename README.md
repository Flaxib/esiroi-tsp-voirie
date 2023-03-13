# WebGIS - Flaxib

WebGIS - Flaxib est une application web de SIG (Système d’Information Géographique) pour l’estimation de la vitesse moyenne des bus sur des tronçons de route. Elle a été créée dans le cadre d’un partenariat entre Flaxib, une jeune startup réunionnaise, et la CINOR (Communauté d’Intercommunalité du Nord de La Réunion).

# Fonctionnalités

L’objectif principal du projet WebGIS - Flaxib est de pouvoir estimer le temps que prend un véhicule pour parcourir un tronçon de route. Pour ce faire, l’application utilise des données géographiques et des algorithmes d’optimisation pour calculer le temps de parcours en fonction du gabarit du véhicule et des conditions de la route.

# Technologies
Le projet WebGIS - Flaxib a été créé à l’aide de plusieurs technologies. Voici une liste non-exhaustive des principales technologies utilisées et comment elles sont utilisées dans le projet:

- **Leaflet** : une bibliothèque JavaScript open-source pour créer des cartes interactives. Elle est utilisée comme interface client pour afficher les données géographiques. [En savoir plus](https://leafletjs.com/).
- **Django** : un framework web Python pour construire des applications web robustes et évolutives. Il est utilisé en tant qu’API pour délivrer les données au client. [En savoir plus](https://www.djangoproject.com/).
- **PostGIS** : une extension de la base de données PostgreSQL pour stocker et manipuler des données géographiques. Elle est utilisée comme base de données pour stocker les données géographiques. [En savoir plus](https://postgis.net/).

# Installation

1. Téléchargez le fichier `troncon_de_route.sql` à partir du lien suivant : https://geoservices.ign.fr/bdtopo#telechargementsqlter. Vous le trouverez dans la section **Département 974 - La Réunion**.
2. Placez le fichier téléchargé dans le répertoire suivant : `BDTOPO_3-0_TOUSTHEMES_SQL_RGR92UTM40S_REU_2022-09-15\BDTOPO\1_DONNEES_LIVRAISON_2022-10-00022\BDT_3-0_SQL_RGR92UTM40S_REU-ED2022-09-15\TRANSPORT\`.
3. Enregistrez le fichier `troncon_de_route.sql` à la racine du projet.
4. Localisez le fichier `.env` dans le répertoire `./serveur/serveur/`.
5. Si vous n’avez pas encore de fichier `.env`, vous pouvez utiliser le fichier exemple`.env` comme modèle. Copiez-le et renommez-le en `.env`.
6. Assurez-vous que toutes les variables d’environnement nécessaires sont définies dans le fichier `.env`.

# Lancement

1. Ouvrez un terminal et naviguez jusqu’au répertoire racine du projet.
2. Exécutez la commande `docker-compose up` pour lancer l’application.

# Démarrage

Une fois l’application lancée, vous pouvez y accéder en ouvrant un navigateur web et en accédant à l’URL indiquée dans le terminal.