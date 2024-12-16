L'application a été developé avec le framework de python django
pour l'executer en local sur votre machine vous devez d'abord installer djando si vous ne l'avez pas 
encore avec la commande suivante:

    pip install django

en suite allez dans le dossier todo (ou se trouve le manage.py)
puis demarer le sever de django pour lancer l'application avec la commande suivante:

    python manage.py runserver ou 
    python3 manage.py runserver pour les sytemes linux

En fin une fois le server lancer vous pouver aller dans votre navigateur et tapez
    127.0.0.1:8000/todo  pour avoir l'interface de l'application.



Detaille technique:
    Systeme d'exploitation utiliser pour le developement : Linux avec la distribution ubuntu 22.04 LTS
    Langage utiliser: Python, HTML, JavaScript
    framework : tailwind pour le frontend et django pour le backend.




Par defaut on a creer 3 taches dans la bases de données pour voir les differents fonctionnement
de l'application premierement quand une tache est en cours c'est a dire le delai de fin n'est pas encore finis
et deuxiemement quant une tache est deja terminer et marquer comme fini et troisemement quant le delai de fin prevu pour une tache
est deja terminer . 
    Nous profitons ainsi pour dire que preciser la date de fin d'une tache n'est pas obligatoire .

    Les couleurs des titres representent les priorités des taches
            Violet: pour faible (low) 
            Vert : pour moyenne (medium) 
            Rouge : pour elevee (high)


 © 2024 Nicefort KETTEGUIA, Inc. All rights reserved. 