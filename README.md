Bien sûr, voici un exemple de fichier README détaillé pour votre mini-projet de chiffrement de fichiers avec gestion dynamique des clés :

```markdown
# Chiffrement de fichiers avec Gestion Dynamique des Clés

Ce script Python permet de chiffrer et déchiffrer le contenu d'un dossier en utilisant la bibliothèque cryptography. Il inclut une gestion dynamique des clés, stockant la clé de manière sécurisée dans un dossier spécifié.

## Prérequis

- Python installé sur votre système. [Télécharger Python](https://www.python.org/downloads/)

## Installation des dépendances

Installez la bibliothèque cryptography en utilisant la commande suivante dans le terminal ou l'invite de commandes :

```bash
pip install cryptography
```

## Utilisation

1. Clonez le projet vers votre machine ou téléchargez le fichier `chiffrement.py`.

2. Ouvrez un terminal ou une invite de commandes et naviguez vers le répertoire contenant `chiffrement.py`.

3. Exécutez le script avec la commande suivante :

```bash
python chiffrement.py
```

Si vous utilisez Python 3, remplacez `python` par `python3`.

4. Le script vérifiera si une clé existe déjà dans le dossier spécifié. Si non, il en générera une nouvelle et la sauvegardera. Sinon, il chargera la clé existante.

5. Le script chiffrera tout le contenu du dossier spécifié.

6. Pour déchiffrer, commentez la ligne de chiffrement et décommentez la ligne de déchiffrement dans le script. Ensuite, exécutez le script à nouveau.

## Personnalisation

- Modifiez le chemin du dossier de clés dans le script en changeant la valeur de la variable `key_folder`.

- Vous pouvez ajuster le nom du fichier de clé généré en modifiant la fonction `save_key_to_file`.

## Sécurité

- Assurez-vous de stocker le dossier de clés dans un emplacement sécurisé.

- Ne partagez pas la clé générée avec des personnes non autorisées.
