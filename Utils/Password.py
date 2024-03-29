import bcrypt

"""
Nom du script: 
    Password.py
Description: 
    Contient les fonctions permettant de crypter les mot de passe en base de donnée ainsi que la fonction 
    permettant la verification entre deux mot de passe crypté
Dernière revue: 
    14 novembre 2023
Par: 
    Yassine Négoce
"""

config_bcrypt = bcrypt.gensalt()


def encode_password(password: str) -> bytes:
    """Fonction qui encode le mot de passe"""
    return bcrypt.hashpw(bytes(password, encoding='utf-8')
                         , config_bcrypt)


def password_check(password_input, hashed_password):
    """Fonction qui verifie la correspondance entre deux string crypté"""
    return bcrypt.checkpw(password_input.encode('utf-8'), hashed_password.encode('utf-8'))
