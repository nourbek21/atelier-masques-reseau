#!/usr/bin/env python3
"""
Vérificateur automatique de l'atelier « Masques réseau ».

Utilisation (dans le terminal) :
    python3 verifier.py 1        → vérifie l'exercice 1
    python3 verifier.py          → affiche ta progression sur tous les exercices

Les bonnes réponses ne sont pas écrites en clair : inutile de chercher ici 😉
"""
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent
ATTENDU = json.loads((RACINE / "outils" / "attendu.json").read_text(encoding="utf-8"))

VERT, ROUGE, JAUNE, GRIS, GRAS, FIN = "\033[32m", "\033[31m", "\033[33m", "\033[90m", "\033[1m", "\033[0m"


class FormatInvalide(Exception):
    """La réponse n'a pas la bonne forme (ce n'est pas forcément faux)."""


# ---------------------------------------------------------------------------
# Mise en forme des réponses : on accepte quelques variantes d'écriture
# ---------------------------------------------------------------------------
def normaliser(type_, brut):
    texte = brut.strip().lower().replace(" ", "")
    if type_ == "int":
        if not re.fullmatch(r"-?\d+", texte):
            raise FormatInvalide("Écris uniquement un nombre entier (exemple : 42).")
        return str(int(texte))
    if type_ == "bin8":
        if not re.fullmatch(r"[01]+", texte):
            raise FormatInvalide("Écris uniquement des 0 et des 1 (exemple : 00110010).")
        if len(texte) != 8:
            raise FormatInvalide(f"Un octet fait toujours 8 bits : tu en as écrit {len(texte)}. "
                                 "Complète avec des 0 à gauche si besoin.")
        return texte
    if type_ == "bin32":
        parties = texte.split(".")
        if len(parties) != 4 or not all(re.fullmatch(r"[01]{8}", p) for p in parties):
            raise FormatInvalide("Écris 4 groupes de 8 bits séparés par des points "
                                 "(exemple : 11000000.10101000.00110010.00110010).")
        return ".".join(parties)
    if type_ == "ip":
        parties = texte.split(".")
        if len(parties) != 4 or not all(re.fullmatch(r"\d{1,3}", p) for p in parties):
            raise FormatInvalide("Écris une adresse en décimal pointé (exemple : 192.168.1.0).")
        if any(int(p) > 255 for p in parties):
            raise FormatInvalide("Chaque nombre d'une adresse IPv4 est compris entre 0 et 255.")
        return ".".join(str(int(p)) for p in parties)
    if type_ == "cidr":
        texte = texte.lstrip("/")
        if not re.fullmatch(r"\d{1,2}", texte) or int(texte) > 32:
            raise FormatInvalide("Écris la notation CIDR, par exemple /24 (entre /0 et /32).")
        return str(int(texte))
    if type_ == "ouinon":
        if texte in ("oui", "o", "yes", "y", "vrai"):
            return "oui"
        if texte in ("non", "n", "no", "faux"):
            return "non"
        raise FormatInvalide("Réponds par « oui » ou « non ».")
    if type_ == "route":
        if texte in ("direct", "directe", "local", "locale"):
            return "direct"
        if texte in ("passerelle", "routeur", "gateway", "router"):
            return "passerelle"
        raise FormatInvalide("Réponds par « direct » ou « passerelle ».")
    return texte


def empreinte(num, qid, canon):
    return hashlib.sha256(f"masque2026:{num}:{qid}:{canon}".encode()).hexdigest()


def lire_reponses(fichier):
    reponses = {}
    if not fichier.exists():
        return reponses
    for ligne in fichier.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*([A-Za-z]?\d+)\s*=\s*(.*?)\s*$", ligne)
        if m and not ligne.lstrip().startswith("#"):
            reponses[m.group(1).upper()] = m.group(2)
    return reponses


# ---------------------------------------------------------------------------
# Vérification d'un exercice à réponses (exercices 0 à 8)
# ---------------------------------------------------------------------------
def verifier_exercice(num, bavard=True):
    ex = ATTENDU["exercices"][num]
    fichier = RACINE / "exercices" / ex["dossier"] / "reponses.txt"
    reponses = lire_reponses(fichier)
    bons = 0
    if bavard:
        print(f"\n{GRAS}Exercice {num} — {ATTENDU['titres'][num]}{FIN}")
        print(f"{GRIS}Fichier lu : exercices/{ex['dossier']}/reponses.txt{FIN}\n")
    for q in ex["questions"]:
        brut = reponses.get(q["id"], "")
        if brut == "":
            if bavard:
                print(f"  ⬜ {q['id']:<3} {GRIS}pas encore répondu — {q['label']}{FIN}")
            continue
        try:
            canon = normaliser(q["type"], brut)
        except FormatInvalide as e:
            if bavard:
                print(f"  {JAUNE}⚠️  {q['id']:<3} « {brut} » : {e}{FIN}")
            continue
        if empreinte(num, q["id"], canon) == q["hash"]:
            bons += 1
            if bavard:
                print(f"  {VERT}✅ {q['id']:<3} correct{FIN}")
        elif bavard:
            print(f"  {ROUGE}❌ {q['id']:<3} « {brut} » n'est pas la bonne réponse.{FIN}")
            print(f"         💡 Indice : {q['indice']}")
    total = len(ex["questions"])
    if bavard:
        afficher_bilan(bons, total)
    return bons, total


def afficher_bilan(bons, total):
    barre = "█" * bons + "░" * (total - bons)
    print(f"\n  Score : {GRAS}{bons}/{total}{FIN}  {barre}")
    if bons == total:
        print(f"  {VERT}{GRAS}🎉 Bravo, exercice terminé ! Pense à enregistrer ton travail "
              f"(commit + push) puis passe au suivant.{FIN}\n")
    else:
        print(f"  {GRIS}Corrige, enregistre le fichier (Ctrl+S) et relance la vérification.{FIN}\n")


# ---------------------------------------------------------------------------
# Exercice 9 : observation du réseau du Codespace
# ---------------------------------------------------------------------------
def verifier_exercice_9(bavard=True):
    fichier = RACINE / "exercices" / "09-bonus-observer-reseau" / "reponses.txt"
    reponses = lire_reponses(fichier)
    bons, total = 0, 5
    if bavard:
        print(f"\n{GRAS}Exercice 9 — {ATTENDU['titres']['9']}{FIN}\n")
    try:
        ip = normaliser("ip", reponses.get("Q1", ""))
        cidr = int(normaliser("cidr", reponses.get("Q2", "")))
    except FormatInvalide:
        if bavard:
            print(f"  {JAUNE}⚠️  Complète d'abord Q1 (adresse IP) et Q2 (CIDR) avec ce que "
                  f"t'affiche la commande « ip -br -4 addr ».{FIN}")
            afficher_bilan(0, total)
        return 0, total
    bons += 2
    if bavard:
        print(f"  {VERT}✅ Q1/Q2 lus : {ip}/{cidr}{FIN}")
    n_ip = int.from_bytes(bytes(int(x) for x in ip.split(".")), "big")
    n_masque = (0xFFFFFFFF << (32 - cidr)) & 0xFFFFFFFF
    def en_ip(n): return ".".join(str(b) for b in n.to_bytes(4, "big"))
    attendus = {
        "Q3": ("ip", en_ip(n_masque), "Convertis le CIDR en masque décimal (voir exercice 3)."),
        "Q4": ("ip", en_ip(n_ip & n_masque), "Fais IP AND masque (voir exercice 5)."),
        "Q5": ("int", str(max(2 ** (32 - cidr) - 2, 0)), "2^(32 − CIDR) − 2 (voir exercice 7)."),
    }
    for qid, (type_, bonne, indice) in attendus.items():
        try:
            ok = normaliser(type_, reponses.get(qid, "")) == bonne
        except FormatInvalide as e:
            if bavard:
                print(f"  {JAUNE}⚠️  {qid}  {e}{FIN}")
            continue
        bons += ok
        if bavard:
            print(f"  {VERT}✅ {qid}  correct{FIN}" if ok else
                  f"  {ROUGE}❌ {qid}  pas encore.{FIN}\n         💡 Indice : {indice}")
    if bavard:
        afficher_bilan(bons, total)
    return bons, total


# ---------------------------------------------------------------------------
# Exercice 10 : on teste les fonctions Python écrites par l'étudiant
# ---------------------------------------------------------------------------
TESTS_10 = [
    ("decimal_vers_binaire", [((50,), "00110010"), ((255,), "11111111"), ((0,), "00000000"), ((10,), "00001010")]),
    ("binaire_vers_decimal", [(("11110000",), 240), (("00110010",), 50), (("11111111",), 255)]),
    ("cidr_vers_masque", [((24,), "255.255.255.0"), ((20,), "255.255.240.0"), ((26,), "255.255.255.192"), ((8,), "255.0.0.0")]),
    ("adresse_reseau", [(("192.168.50.50", "255.255.255.0"), "192.168.50.0"),
                        (("192.168.50.50", "255.255.240.0"), "192.168.48.0"),
                        (("10.1.203.5", "255.255.252.0"), "10.1.200.0")]),
    ("meme_reseau", [(("192.168.1.10", "192.168.1.250", "255.255.255.0"), True),
                     (("192.168.1.10", "192.168.2.10", "255.255.255.0"), False),
                     (("192.168.1.10", "192.168.2.10", "255.255.0.0"), True)]),
    ("nombre_hotes", [((24,), 254), ((26,), 62), ((20,), 4094)]),
]


def verifier_exercice_10(bavard=True):
    chemin = RACINE / "exercices" / "10-bonus-python" / "mon_calculateur.py"
    total = len(TESTS_10)
    if bavard:
        print(f"\n{GRAS}Exercice 10 — {ATTENDU['titres']['10']}{FIN}\n")
    try:
        spec = importlib.util.spec_from_file_location("mon_calculateur", chemin)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    except Exception as e:  # erreur de syntaxe, etc.
        if bavard:
            print(f"  {ROUGE}❌ Ton fichier contient une erreur : {type(e).__name__} : {e}{FIN}")
            afficher_bilan(0, total)
        return 0, total
    bons = 0
    for nom, cas in TESTS_10:
        fonction = getattr(module, nom, None)
        probleme = None
        for args, attendu in cas:
            try:
                obtenu = fonction(*args)
            except Exception as e:
                probleme = f"{nom}{args} provoque une erreur : {type(e).__name__} : {e}"
                break
            if obtenu != attendu:
                probleme = f"{nom}{args} renvoie {obtenu!r}, attendu {attendu!r}"
                break
        if probleme is None:
            bons += 1
            if bavard:
                print(f"  {VERT}✅ {nom}{FIN}")
        elif bavard:
            print(f"  {ROUGE}❌ {probleme}{FIN}")
    if bavard:
        afficher_bilan(bons, total)
    return bons, total


# ---------------------------------------------------------------------------
def progression():
    print(f"\n{GRAS}📊 Ta progression{FIN}\n")
    for num in sorted(ATTENDU["titres"], key=int):
        bons, total = verifier(num, bavard=False)
        etat = "🎉" if bons == total else ("🟡" if bons else "⬜")
        print(f"  {etat} Exercice {num:>2} — {ATTENDU['titres'][num]:<42} {bons:>2}/{total}")
    print(f"\n{GRIS}Pour le détail d'un exercice : python3 verifier.py <numéro>{FIN}\n")


def verifier(num, bavard=True):
    if num == "9":
        return verifier_exercice_9(bavard)
    if num == "10":
        return verifier_exercice_10(bavard)
    return verifier_exercice(num, bavard)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        progression()
    elif sys.argv[1].lstrip("0") in ATTENDU["titres"] or sys.argv[1] in ATTENDU["titres"]:
        verifier(sys.argv[1].lstrip("0") or "0")
    else:
        print(f"Exercice inconnu : {sys.argv[1]}. Exemple : python3 verifier.py 1")
