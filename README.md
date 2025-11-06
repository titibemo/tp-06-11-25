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
il crééra un container se nommant tp-06-11-25 contenant un sous-container avec un nom: read-write, notre container d'exercice.

enfin, pour intéragir avec le projet, rendez-vous sur votre plateforme docker, ouvrez un terminal (en bas à droite) et effectuez les commandes suivantes:

```bash
docker start read-write
```
Pour allumer votre conteneur si celui-ci n'est pas allumé.

```bash
docker exec -it read-write bash
```
Pour rentrer dans le terminal du container

```bash
python main.py
```
Pour activer le script, vous pouvez alors intéragir avec l'exercice.

## Fin et suppression

Une fois après avoir quitté l'application, n'oubliez pas d'arrêter ou de supprimer le conteneur avec les deux commandes suivantes :

```bash
docker stop read-write
```
Pour stopper le container.


```bash
docker rm read-write
```
Pour supprimer le container. *Même en étant supprimé, Les données sont sauvegardées !*

```bash
docker volume rm tp-06-11-25_tp-volume
```
Pour supprimer définitivement le volume et les données associées.

