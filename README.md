# VanillaUnicorn
## Projet web sur flask 
## Lancer l'application web
 Installer un virtualenv avec la commande `virtualenv -p python3 venv` 
 Si vous avez venv, vous pouvez lancez votre environnement avec ` source venv/bin/activate` (.venv/Scripts/Activte sur Windows),
 deplacer vous dans le dossier VanillaUnicorn
 Une fois sur votre virtualenv,lancer la commande `pip install requirements.txt`.
 Maintenant vous avez toute les extensions pour lancer Flask donc faite la commande `Flask run`
 un url va s'afficher faite un ctrl+click pour ouvrir la page
 maintenant vous étes connéctés ! 
## Pour ajouter un utilisateur
`flask newuser name password`
### Pour se Connecter
si votre compte existe alors appuyer sur le bouton login, renseigner les champs et appuyer sur entrer,
votre nom d'utilisateurs doit s'afficher en haut à droite ansi qu'un bouton `logout` pour se déconnecter.
### Pour editer un livre
appuyer sur l'image du livre voulu puis appuyer sur le bouton edit en bas a gauche.
### Pour faire une recherche 
dans le chemin de l'url changer en `http://127.0.0.1:5000/recherche/`avec la recherche de votre choix (auteur, partie du nom du livre)
