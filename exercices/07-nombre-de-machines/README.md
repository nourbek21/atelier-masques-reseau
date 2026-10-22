# Exercice 7 — Combien de machines ? ⭐⭐

⏱️ 20 minutes · 🎯 Objectif : calculer la taille d'un réseau et choisir le bon masque.

## 📖 Rappel

```text
Bits hôtes          = 32 − CIDR
Nombre d'adresses   = 2 ^ (bits hôtes)
Hôtes utilisables   = 2 ^ (bits hôtes) − 2
```

On retire **2** adresses réservées : l'**adresse réseau** (la première) et l'**adresse de broadcast** (la dernière).

Puissances de 2 utiles :

```text
2^1 = 2      2^5 = 32     2^9  = 512
2^2 = 4      2^6 = 64     2^10 = 1024
2^3 = 8      2^7 = 128    2^11 = 2048
2^4 = 16     2^8 = 256    2^12 = 4096
```

> 🧠 Chaque bit hôte en plus **double** le nombre d'adresses.

## ✍️ Exemple résolu : un /25

```text
Bits hôtes        = 32 − 25 = 7
Nombre d'adresses = 2^7     = 128
Hôtes utilisables = 128 − 2 = 126
```

## ✍️ Exemple résolu : il faut connecter 100 machines

On cherche le **plus petit** réseau qui suffit :

```text
/26 → 2^6 − 2 =  62 hôtes  ❌ pas assez
/25 → 2^7 − 2 = 126 hôtes  ✅ suffisant
```

Réponse : **/25**

## 📝 À toi !

| Question | Énoncé |
|---|---|
| **Q1** | Nombre d'**adresses** dans un `/24` |
| **Q2** | Nombre d'**hôtes utilisables** dans un `/24` |
| **Q3** | Nombre d'hôtes utilisables dans un `/22` |
| **Q4** | Nombre d'hôtes utilisables dans un `/26` |
| **Q5** | Nombre d'hôtes utilisables dans un `/30` |
| **Q6** | Plus petit réseau (CIDR) pour **300** machines |
| **Q7** | Plus petit réseau (CIDR) pour **50** machines |
| **Q8** | Plus petit réseau (CIDR) pour **1000** machines |

📄 Réponds dans [`reponses.txt`](reponses.txt) puis vérifie :

```bash
python3 verifier.py 7
```

> 🤓 **Le savais-tu ?** Le `/30` (Q5) est souvent utilisé pour relier **deux routeurs** entre eux : il n'y a besoin que de 2 adresses !

---

➡️ Exercice suivant : [08 — Défi : la carte d'identité d'un réseau](../08-defi-carte-reseau/README.md)
