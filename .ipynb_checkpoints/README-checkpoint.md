# TP 06-11-2025

1. Projet
2. prérequis
3. installation & utilisation
4. Fin et suppression

## Projet

Ce projet permet de mettre en évidence l'utilisation des fonctionnalités de python et de docker. Vous pourrez dans ce projet entre autres :
- utiliser l'application pour, voir, éditer, supprimer et ajouter des films dans une base de film ajoutée dans movies.csv
- rechercher par titre les films. 

## prérequis

Vous devez avoir docker et git installé sur votre ordinateur, si cela n'est pas le cas, rendez-vous à ces adresses afin de télécharger la version adéquate pour votre système d'exploitation sur votre ordinateur:

https://www.docker.com/

https://git-scm.com/


## Installation & utilisation

Dans un premier temps, vous devez cloner le projet sur votre ordinateur pour cela faite :

```bash
git clone https://github.com/titibemo/tp-06-11-25
```

Une fois cloné, ouvrez le dossier sur votre éditeur de texte.
à la racine du dossier, ouvrez un terminal de commande et effectuez la commande suivante pour créer l'image ainsi que le container :

```bash
docker compose up -d
```
il crééra un container se nommant tp-06-11-25 contenant un sous-container avec un nom: read-write, ne vous en souciez pas.

enfin, pour intéragir avec le projet, rendez-vous sur votre plateforme docker, ouvrez un terminal (en bas à droite) et effectuez la commande suivante:

```bash
docker run -it -p 8089:5000 --name tp-06-11-25  tp-06-11-25-read
```
il crééra un conteneur (se nommant tp-06-11-25) avec l'image créé précédemment. Vous devriez pouvoir, depuis le terminal de docker, utiliser le projet.


## Fin et suppression

Une fois après avoir quitté l'application, n'oubliez pas de supprimer le conteneur avec les deux commandes suivantes :

```bash
docker rm tp-06-11-25
docker rm read-write
```
