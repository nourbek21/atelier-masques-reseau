# Exercice 5 — Trouver l'adresse réseau ⭐⭐

⏱️ 25 minutes · 🎯 Objectif : calculer l'adresse réseau d'une machine avec **IP AND masque**.

## 📖 Rappel

```text
Adresse IP  AND  Masque  =  Adresse réseau
```

On fait le AND **octet par octet**. Grâce à l'exercice 4, on connaît des raccourcis :

| Octet du masque | Ce qu'on fait |
|---|---|
| `255` | On **recopie** l'octet de l'IP |
| `0` | On écrit **0** |
| autre valeur (128, 192, 224, 240…) | On fait le **AND en binaire** sur cet octet uniquement |

## ✍️ Exemple résolu facile : 192.168.5.77/24

Masque `/24` = `255.255.255.0`

```text
IP     : 192 . 168 .  5 . 77
Masque : 255 . 255 . 255 .  0
         recopie recopie recopie → 0
Réseau : 192 . 168 .  5 .  0
```

Adresse réseau : **192.168.5.0**

## ✍️ Exemple résolu difficile : 172.20.130.15/20

Masque `/20` = `255.255.240.0`

```text
IP     : 172 . 20 . 130 . 15
Masque : 255 . 255 . 240 .  0
          ↓     ↓     ?     ↓
         172 . 20  .  ?  .  0
```

Il reste le 3e octet : `130 AND 240`

```text
     130 = 1 0 0 0 0 0 1 0
AND 240 = 1 1 1 1 0 0 0 0
          ---------------
          1 0 0 0 0 0 0 0  = 128
```

Adresse réseau : **172.20.128.0**

> ⚠️ Piège classique : ce n'est **pas** `172.20.130.0` ! Quand la frontière passe au milieu d'un octet, il faut faire le calcul en binaire.

## 📝 À toi !

| Question | Adresse | Indication |
|---|---|---|
| **Q1** | `192.168.10.37/24` | facile |
| **Q2** | `172.16.45.12/16` | facile |
| **Q3** | `10.20.30.40/8` | facile |
| **Q4** | `192.168.50.50/20` | l'exemple du cours |
| **Q5** | `192.168.77.130/20` | 🧮 binaire |
| **Q6** | `10.1.203.5/22` | 🧮 binaire |
| **Q7** | `192.168.1.200/25` | 🧮 binaire, 4e octet |

📄 Réponds dans [`reponses.txt`](reponses.txt) puis vérifie :

```bash
python3 verifier.py 5
```

---

➡️ Exercice suivant : [06 — Même réseau ?](../06-meme-reseau/README.md)
