# Utiliser une image Alpine Python
FROM python:3-alpine3.15

# Définir le répertoire de travail
WORKDIR /app

# Installer des outils de compilation nécessaires
RUN apk add --no-cache gcc g++ musl-dev linux-headers gfortran lapack-dev openblas-dev

# Copier les fichiers du projet
COPY . /app

# Installer les dépendances du fichier requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exposer le port utilisé par votre application Flask
EXPOSE 5001

# Commande pour exécuter l'application Flask
CMD ["python", "./app.py"]
