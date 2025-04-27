# Gestion container

| Fonction                          | Commande |
| :--------------                   | :--------------- |
| Construire l'image                | docker build -t y4nc/theta-app:0.0.3 . |
| Créer et démarrer le container    | docker run --rm --name container-theta-app y4nc/theta-app:0.0.3 |
| Arrêter un container              | docker stop theta-app |
| Lister les containers             | docker ps -a |
| Entrer dans le container          | docker exec -it container-theta-app /bin/bash |
| Lire un fichier dans le container | cat flows.csv |


# Docker Hub

| Fonction                              | Commande |
| :--------------                       | :--------------- |
| Se connecter à Docker Hub             | docker login |
| Publier une image sur Docker Hub      | docker push y4nc/theta-app:0.0.3 |
| Récupérer une image depuis Docker Hub | docker pull y4nc/theta-app:0.0.3 |







