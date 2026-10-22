# Exercice 1 — Du décimal au binaire (un octet) ⭐

⏱️ 15 minutes · 🎯 Objectif : convertir un nombre entre 0 et 255 en binaire (8 bits), et inversement.

## 📖 Rappel

Un **octet** = 8 bits. Chaque position a un **poids** :

```text
Position :  1    2    3    4    5    6    7    8
Poids    : 128   64   32   16    8    4    2    1
```

- Un bit à `1` → on **compte** le poids.
- Un bit à `0` → on **ne compte pas** le poids.

## ✍️ Exemple résolu : 50 en binaire

On cherche quels poids additionner pour obtenir 50, **en partant de la gauche** :

```text
128 ? trop grand (128 > 50)            → 0
 64 ? trop grand (64 > 50)             → 0
 32 ? oui → il reste 50 - 32 = 18      → 1
 16 ? oui → il reste 18 - 16 = 2       → 1
  8 ? trop grand (8 > 2)               → 0
  4 ? trop grand (4 > 2)               → 0
  2 ? oui → il reste 2 - 2 = 0         → 1
  1 ? il ne reste rien                 → 0
```

```text
Poids :  128 64 32 16  8  4  2  1
Bits  :    0  0  1  1  0  0  1  0     →   50 = 00110010
```

## ✍️ Exemple résolu : 11000000 en décimal

```text
Poids :  128 64 32 16  8  4  2  1
Bits  :    1  1  0  0  0  0  0  0
```

On additionne les poids où il y a un `1` : 128 + 64 = **192**.

## 📝 À toi !

Écris toujours **8 bits** (avec des 0 à gauche si besoin : `10` s'écrit `00001010`, pas `1010`).

**Décimal → binaire**

| Question | Convertir en binaire |
|---|---|
| **Q1** | 128 |
| **Q2** | 192 |
| **Q3** | 255 |
| **Q4** | 10 |
| **Q5** | 168 |

**Binaire → décimal**

| Question | Convertir en décimal |
|---|---|
| **Q6** | 11110000 |
| **Q7** | 00110000 |
| **Q8** | 11111100 |
| **Q9** | 01100100 |

📄 Réponds dans [`reponses.txt`](reponses.txt) puis vérifie :

```bash
python3 verifier.py 1
```

> 🧠 **À remarquer** : les nombres 128, 192, 224, 240, 248, 252, 254, 255 reviendront **tout le temps** dans les masques. Ce sont des 1 « collés à gauche » !

---

➡️ Exercice suivant : [02 — Une adresse IP en binaire](../02-ip-en-binaire/README.md)
