"""
Exercice 10 — Mon calculateur de masques réseau

Complète chaque fonction à la place de « pass » (cherche les TODO).
Vérifie avec :  python3 verifier.py 10
"""


def decimal_vers_binaire(n):
    """Renvoie l'octet n (entre 0 et 255) écrit sur 8 bits.
    Exemple : decimal_vers_binaire(50) → "00110010"
    """
    # TODO
    pass


def binaire_vers_decimal(bits):
    """Renvoie la valeur décimale d'une chaîne de 8 bits.
    Exemple : binaire_vers_decimal("11110000") → 240
    """
    # TODO
    pass


def cidr_vers_masque(cidr):
    """Renvoie le masque en décimal pointé.
    Exemple : cidr_vers_masque(20) → "255.255.240.0"

    Piste : construis une chaîne de cidr fois "1" suivie de (32 - cidr) fois "0",
    découpe-la en 4 morceaux de 8 bits, puis convertis chaque morceau.
    """
    # TODO
    pass


def adresse_reseau(ip, masque):
    """Renvoie l'adresse réseau (IP AND masque, octet par octet).
    Exemple : adresse_reseau("192.168.50.50", "255.255.240.0") → "192.168.48.0"
    """
    # TODO
    pass


def meme_reseau(ip1, ip2, masque):
    """Renvoie True si ip1 et ip2 sont sur le même réseau, sinon False.
    Exemple : meme_reseau("192.168.1.10", "192.168.2.10", "255.255.0.0") → True

    Piste : réutilise adresse_reseau !
    """
    # TODO
    pass


def nombre_hotes(cidr):
    """Renvoie le nombre d'hôtes utilisables.
    Exemple : nombre_hotes(24) → 254
    """
    # TODO
    pass


# Ce bloc s'exécute quand tu lances : python3 exercices/10-bonus-python/mon_calculateur.py
if __name__ == "__main__":
    print("50 en binaire     :", decimal_vers_binaire(50))
    print("11110000          :", binaire_vers_decimal("11110000"))
    print("/20               :", cidr_vers_masque(20))
    print("Réseau            :", adresse_reseau("192.168.50.50", "255.255.240.0"))
    print("Même réseau ?     :", meme_reseau("192.168.1.10", "192.168.2.10", "255.255.0.0"))
    print("Hôtes dans un /24 :", nombre_hotes(24))
