from cryptography.fernet import Fernet
import os
import hashlib

def generate_key():
    """
    Fonction pour générer une clé de chiffrement Fernet .
    """
    return Fernet.generate_key()

def save_key_to_file(key, folder_path):
    """
    Fonction pour enregistrer la clé dans un fichier avec un nom dynamique.
    """
    # Utilisation du hachage MD5 de la clé comme identifiant unique pour le nom de fichier
    hash_object = hashlib.md5(key)
    file_name = f"{hash_object.hexdigest()}_key.txt"
    
    file_path = os.path.join(folder_path, file_name)
    
    with open(file_path, 'wb') as file:
        file.write(key)
        
def load_key_from_file(folder_path):
    """
    Fonction pour charger la clé depuis un fichier avec un nom dynamique.
    """
    
    # Listez tous les fichiers dans le dossier
    files = os.listdir(folder_path)
    
    # Si aucun fichier n'est trouvé, retournez None
    if not files:
        return None
    
    # Triez les fichiers par ordre alphabétique pour obtenir le plus récent en dernier
    files.sort()
    
    # Obenez le dernier fichier (qui devrais être le plus récent)
    latest_file = files[-1]
    
    # construisez le chemin complet du fichier
    file_path = os.path.join(folder_path, latest_file)
    
    # Lisez la clé depuis le fichier
    with open(file_path, 'rb') as file:
        return file.read()

def encrypt_folder(key, folder_path):
    """
    Fonction pour chiffrer tout le contenu d'un dossier (y compris les sous dossiers et fichiers).
    """
    cipher_suite = Fernet(key)
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            with open(file_path, 'rb') as file:
                file_data = file.read()
            encrypted_data = cipher_suite.encrypt(file_data)
            with open(file_path, 'wb') as file:
                file.write(encrypted_data)
    print("Cryptage is done !")

def decrypt_folder(key, folder_path):
    """
    Fonction pour déchiffer tout le contenu d'un dossier (y compris les sous-dossier et fichiers).
    """
    cipher_suite = Fernet(key)
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            with open(file_path, 'rb') as file:
                file_data = file.read()
            decrypted_data = cipher_suite.decrypt(file_data)
            with open(file_path, 'wb') as file:
                file.write(decrypted_data)
    print("Decryptage is done !")

# Spécifiez le chemin du dossier pour stocker les fichiers de clé
key_folder = 'C:/Users/aymar.adjaho/Desktop/cryptography/key_folder'

# Générer une clé si elle n'existe pas 
if not os.path.exists(key_folder):
    os.makedirs(key_folder)
    
key = load_key_from_file(key_folder)

# Si aucune clé n'est trouvé, générer une nouvelle clé et l'enregistrer
if key is None:
    key = generate_key()
    save_key_to_file(key, key_folder)



                
# Exemple d'utilisation

# Générer une clé (veillez à stocker en toute sécurité cette clé, ne la partagez pas avec d'autres)
# key = generate_key()

# Chiffrer tout le contenu du dossier spécifé (y compris les sous-dossiers et fichiers)
decrypt_folder(key, 'C:/Users/aymar.adjaho/Desktop/test')

# Pour décrypter, utilisez decrypt_folder avec la même clé
# decrypt_folder(key, '/chemin/vers/dossier')