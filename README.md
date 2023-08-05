# slotbot - Bot de réservation de créneaux de correction pour 42Paris (Python)
A bot that gets slots!

SlotBot est un bot Python qui automatise le processus de réservation des créneaux de correction pour le jour meme. Il utilise la bibliothèque Selenium pour interagir avec un navigateur Chrome ou Chromium et effectuer les actions nécessaires.

## Prérequis

- Python 3.x installé sur votre système.
- [Selenium](https://www.selenium.dev/documentation/en/) : Vous pouvez l'installer à l'aide de `pip` en exécutant la commande suivante :
 ```bash
   pip install selenium
```
- Chrome ou Chromium : Vous aurez besoin d'installer l'un de ces navigateurs et de disposer du driver approprié pour Selenium.

## Installation

1. Clonez ce dépôt GitHub ou téléchargez le fichier `slotbot.py`.

## Utilisation

1. Assurez-vous d'avoir installé les dépendances requises (Python 3.x et Selenium).

2. Exécutez le script `slotbot.py` en utilisant la commande suivante :

```bash
python slotbot.py
```
Le script vous demandera les informations suivantes :
- Nom du projet : Entrez le nom du projet pour lequel vous souhaitez organiser les corrections.
- Nombre de créneaux demandés : Entrez le nombre de créneaux que vous souhaitez réserver pour les corrections.
- Nom d'utilisateur : Saisissez votre nom d'utilisateur pour vous connecter au système de réservation.
- Mot de passe : Saisissez votre mot de passe associé à votre nom d'utilisateur.

SlotBot utilisera alors Selenium pour ouvrir le navigateur Chrome/Chromium, se connecter au système de réservation de l'intra et réservera le premier creneaux disponible le jour meme.
SlotBot continuera a rafraichir la page jusqu'a ce que le nombre de créneaux voulu soit atteint.

## Remarque

Assurez-vous de respecter les conditions d'utilisation de l'intra et de 42.fr. L'utilisation de bots pour automatiser des tâches en ligne peut être soumise à des restrictions ou des interdictions dans certains cas. 
Utilisez ce script à vos risques et périls, et prenez les mesures appropriées pour respecter les politiques du système concerné.

## Auteur
Ce script a été créé par Alexis LOUBIERE. 42id: aloubier

N'hésitez pas à améliorer ce script selon vos besoins et faites moi part de vos retours via github ou discord/slack.

## Licence

Ce projet est sous licence GPLv3.0. Consultez le fichier LICENSE pour plus d'informations.
