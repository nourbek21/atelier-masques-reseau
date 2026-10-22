# Exercice 6 — Même réseau ? Direct ou passerelle ? ⭐⭐

⏱️ 20 minutes · 🎯 Objectif : décider, comme le fait un ordinateur, si une destination est **locale** ou s'il faut passer par la **passerelle** (le routeur).

## 📖 Rappel

Pour savoir si deux machines sont sur le même réseau :

1. On calcule l'adresse réseau de la **première** machine (IP AND masque).
2. On calcule l'adresse réseau de la **deuxième** machine (avec le **même** masque).
3. On compare :

```text
             Même adresse réseau ?
                 /         \
               OUI         NON
                │            │
         envoi DIRECT    envoi à la PASSERELLE
```

## ✍️ Exemple résolu 1 : 192.168.10.5 et 192.168.10.200 en /24

```text
192.168.10.5   AND 255.255.255.0 = 192.168.10.0
192.168.10.200 AND 255.255.255.0 = 192.168.10.0
```

Identiques → **même réseau** → envoi **direct**.

## ✍️ Exemple résolu 2 : 172.16.20.1 et 172.16.40.1 en /20

Masque : `255.255.240.0`. Seul le 3e octet demande un calcul :

```text
20 AND 240 :  00010100 AND 11110000 = 00010000 = 16  → 172.16.16.0
40 AND 240 :  00101000 AND 11110000 = 00100000 = 32  → 172.16.32.0
```

Différents → **réseaux différents** → envoi à la **passerelle**.

## 📝 À toi !

**Q1 à Q5 : réponds par `oui` ou `non`** — les deux machines sont-elles sur le même réseau ?

| Question | Machine 1 | Machine 2 | Masque |
|---|---|---|---|
| **Q1** | `192.168.1.10` | `192.168.1.250` | `/24` |
| **Q2** | `192.168.1.10` | `192.168.2.10` | `/24` |
| **Q3** | `192.168.1.10` | `192.168.2.10` | `/16` |
| **Q4** | `192.168.50.10` | `192.168.60.20` | `/20` |
| **Q5** | `192.168.50.10` | `192.168.70.1` | `/20` |

> 🧠 Compare Q2 et Q3 : **mêmes adresses, masque différent, réponse différente !** C'est tout l'intérêt du masque.

**Q6 et Q7 : réponds par `direct` ou `passerelle`**

Le PC de Léa a l'adresse `10.0.5.20/22`.

| Question | Léa envoie un message à… |
|---|---|
| **Q6** | `10.0.7.200` |
| **Q7** | `10.0.8.1` |

📄 Réponds dans [`reponses.txt`](reponses.txt) puis vérifie :

```bash
python3 verifier.py 6
```

---

➡️ Exercice suivant : [07 — Combien de machines ?](../07-nombre-de-machines/README.md)
