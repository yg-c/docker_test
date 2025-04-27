# Image officielle Python 3.12
FROM python:3.12-slim

# Définir le fuseau horaire en premier pour que ça s’applique partout
ENV TZ=Europe/Zurich
RUN apt-get update && apt-get install -y tzdata && rm -rf /var/lib/apt/lists/*

# Définir le code client
ENV CLIENT_CODE="THETA"

# Répertoire de travail dans le conteneur
WORKDIR /app

# Copier tous les fichiers de l'application
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Commande de démarrage
CMD ["python3", "main.py"]
