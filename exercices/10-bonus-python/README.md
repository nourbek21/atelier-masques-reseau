# Exercice 10 — Bonus : programmer son calculateur ⭐⭐⭐

⏱️ 30 à 45 minutes · 🎯 Objectif : écrire en **Python** les calculs que tu as faits à la main.

> Cet exercice est pour celles et ceux qui ont fini et qui connaissent un peu Python. Il n'est **pas obligatoire**.

## 📖 Ce qu'il faut savoir en Python

```python
# Le AND bit à bit s'écrit &
print(50 & 240)            # 48

# Écrire un nombre en binaire sur 8 bits
print(format(50, "08b"))   # '00110010'

# Lire un nombre écrit en binaire
print(int("00110010", 2))  # 50

# Découper une adresse IP en 4 nombres
octets = [int(x) for x in "192.168.1.10".split(".")]   # [192, 168, 1, 10]

# Recoller 4 nombres en adresse IP
print(".".join(str(x) for x in [192, 168, 1, 0]))      # '192.168.1.0'

# Puissance : 2^8 s'écrit 2 ** 8
print(2 ** 8)              # 256
```

## 📝 À toi !

Ouvre [`mon_calculateur.py`](mon_calculateur.py) et complète les **6 fonctions** (cherche les `TODO`).

Vérifie au fur et à mesure :

```bash
python3 verifier.py 10
```

Tu peux aussi tester directement ton fichier :

```bash
python3 exercices/10-bonus-python/mon_calculateur.py
```

🏆 Défi ultime : ajoute une fonction `broadcast(ip, masque)`. Indice : l'opérateur `~` inverse les bits, et `255 - x` inverse les bits d'un octet !
