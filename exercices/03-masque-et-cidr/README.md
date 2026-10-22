# Exercice 3 — Le masque : binaire et notation CIDR ⭐⭐

⏱️ 20 minutes · 🎯 Objectif : passer d'un masque décimal (`255.255.255.0`) à la notation CIDR (`/24`), et inversement.

## 📖 Rappel

Dans un masque :

```text
1 = partie réseau
0 = partie machine (hôte)
```

Les `1` sont **toujours à gauche**, les `0` **toujours à droite**, sans mélange :

```text
11111111.11111111.11111111.00000000   ✅ masque valide
11111111.11111111.00000000.11111111   ❌ pas un masque !
```

La notation **CIDR** `/n` donne simplement le **nombre de bits à 1**.

Valeurs à connaître pour un octet :

```text
00000000 =   0   (0 bit à 1)
10000000 = 128   (1 bit à 1)
11000000 = 192   (2 bits à 1)
11100000 = 224   (3 bits à 1)
11110000 = 240   (4 bits à 1)
11111000 = 248   (5 bits à 1)
11111100 = 252   (6 bits à 1)
11111110 = 254   (7 bits à 1)
11111111 = 255   (8 bits à 1)
```

## ✍️ Exemple résolu : 255.255.255.0 → CIDR

```text
11111111.11111111.11111111.00000000
   8    +   8    +   8    +   0     = 24   →  /24
```

## ✍️ Exemple résolu : /21 → masque décimal

21 = 8 + 8 + **5** → deux octets pleins, puis 5 bits à 1 dans le 3e octet :

```text
11111111.11111111.11111000.00000000
   255  .  255   .  248   .   0     →  255.255.248.0
```

## 📝 À toi !

Pour le CIDR, tu peux écrire `/24` ou `24`.

| Question | Énoncé |
|---|---|
| **Q1** | `255.255.255.0` → CIDR ? |
| **Q2** | `255.255.0.0` → CIDR ? |
| **Q3** | `/8` → masque décimal ? |
| **Q4** | `255.255.255.128` → CIDR ? |
| **Q5** | `/20` → masque décimal ? |
| **Q6** | `/22` → masque décimal ? |
| **Q7** | `/26` → masque décimal ? |
| **Q8** | Combien de **bits hôtes** dans un `/20` ? |
| **Q9** | `255.255.0.255` est-il un masque valide ? (`oui` / `non`) |

📄 Réponds dans [`reponses.txt`](reponses.txt) puis vérifie :

```bash
python3 verifier.py 3
```

---

➡️ Exercice suivant : [04 — L'opération AND](../04-operation-and/README.md)
