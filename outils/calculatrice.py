#!/usr/bin/env python3
"""
Calculatrice de masques réseau qui montre les calculs en binaire.

Utilisation :
    python3 outils/calculatrice.py 192.168.50.50/20
    python3 outils/calculatrice.py 192.168.50.50 255.255.240.0
"""
import sys

VERT, BLEU, GRIS, GRAS, FIN = "\033[32m", "\033[34m", "\033[90m", "\033[1m", "\033[0m"


def vers_entier(ip):
    octets = [int(x) for x in ip.split(".")]
    if len(octets) != 4 or any(not 0 <= o <= 255 for o in octets):
        raise ValueError
    return int.from_bytes(bytes(octets), "big")


def vers_ip(n):
    return ".".join(str(b) for b in n.to_bytes(4, "big"))


def en_binaire(n, cidr):
    """Binaire pointé, avec la partie réseau en bleu et la partie hôte en vert."""
    bits = format(n, "032b")
    texte = ""
    for i, b in enumerate(bits):
        if i and i % 8 == 0:
            texte += "."
        if i == cidr:
            texte += f"{GRAS}|{FIN}"
        texte += f"{BLEU if i < cidr else VERT}{b}{FIN}"
    return texte


def lire_arguments(args):
    if len(args) == 1 and "/" in args[0]:
        ip, cidr = args[0].split("/")
        return vers_entier(ip), int(cidr)
    if len(args) == 2:
        masque = format(vers_entier(args[1]), "032b")
        if "01" in masque:
            raise ValueError("masque invalide : les 1 doivent être tous à gauche")
        return vers_entier(args[0]), masque.count("1")
    raise ValueError


def main():
    try:
        ip, cidr = lire_arguments(sys.argv[1:])
        if not 0 <= cidr <= 32:
            raise ValueError
    except ValueError as e:
        print(__doc__)
        if str(e):
            print(f"Erreur : {e}")
        return

    masque = (0xFFFFFFFF << (32 - cidr)) & 0xFFFFFFFF
    reseau = ip & masque
    broadcast = reseau | (~masque & 0xFFFFFFFF)
    bits_hotes = 32 - cidr
    nb_adresses = 2 ** bits_hotes

    print(f"\n{GRAS}Calcul pour {vers_ip(ip)}/{cidr}{FIN}")
    print(f"{GRIS}En bleu : partie réseau · en vert : partie hôte · | = frontière{FIN}\n")
    print(f"  Adresse IP  {vers_ip(ip):>15}   {en_binaire(ip, cidr)}")
    print(f"  Masque  AND {vers_ip(masque):>15}   {en_binaire(masque, cidr)}")
    print(f"  {'-' * 66}")
    print(f"  Réseau   =  {vers_ip(reseau):>15}   {en_binaire(reseau, cidr)}\n")
    print(f"  Notation CIDR     : /{cidr}  ({cidr} bits réseau, {bits_hotes} bits hôtes)")
    print(f"  Adresse réseau    : {vers_ip(reseau)}")
    if nb_adresses > 2:
        print(f"  Premier hôte      : {vers_ip(reseau + 1)}")
        print(f"  Dernier hôte      : {vers_ip(broadcast - 1)}")
    print(f"  Broadcast         : {vers_ip(broadcast)}   {GRIS}(tous les bits hôtes à 1){FIN}")
    print(f"  Nombre d'adresses : 2^{bits_hotes} = {nb_adresses}")
    print(f"  Hôtes utilisables : {nb_adresses} - 2 = {max(nb_adresses - 2, 0)}\n")


if __name__ == "__main__":
    main()
