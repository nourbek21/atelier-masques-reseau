# Exercice 8 — Défi : la carte d'identité d'un réseau ⭐⭐⭐

⏱️ 30 minutes · 🎯 Objectif : tout combiner pour décrire complètement un réseau.

Pour une adresse donnée, on veut sa **carte d'identité** :

| Information | Comment la trouver |
|---|---|
| Adresse réseau | IP AND masque (exercice 5) — tous les bits hôtes à **0** |
| Premier hôte | Adresse réseau **+ 1** |
| Broadcast | Tous les bits hôtes à **1** |
| Dernier hôte | Broadcast **− 1** |
| Nombre d'hôtes | 2^(bits hôtes) − 2 (exercice 7) |

## 💡 Astuce : la taille du bloc

Regarde l'octet du masque qui **n'est ni 255 ni 0** (l'octet « intéressant ») :

```text
Taille du bloc = 256 − valeur de cet octet
```

Les réseaux commencent alors à des multiples de cette taille : 0, taille, 2×taille, 3×taille…
Le broadcast est la **dernière adresse du bloc** : début du bloc + taille − 1 (et les octets suivants à 255).

> Si le masque ne contient que des 255 et des 0 (ex. `/24`), l'octet intéressant est le premier octet à 0, et la taille du bloc est 256.

## ✍️ Exemple résolu : 192.168.20.130/25

Masque `/25` = `255.255.255.128` → octet intéressant : le 4e (128).
Taille du bloc = 256 − 128 = **128** → les réseaux commencent à .0, .128

130 est entre 128 et 255, donc :

```text
Adresse réseau : 192.168.20.128
Premier hôte   : 192.168.20.129
Broadcast      : 192.168.20.255   (128 + 128 − 1 : dernière adresse du bloc)
Dernier hôte   : 192.168.20.254
Nombre d'hôtes : 2^7 − 2 = 126
```

## ✍️ Exemple résolu : 192.168.50.50/20 (celui du cours)

Masque `/20` = `255.255.240.0` → octet intéressant : le 3e (240).
Taille du bloc = 256 − 240 = **16** → les réseaux commencent à 0, 16, 32, **48**, 64…

50 est entre 48 et 63, donc :

```text
Adresse réseau : 192.168.48.0
Premier hôte   : 192.168.48.1
Broadcast      : 192.168.63.255   (48 + 16 − 1 = 63 : dernière adresse du bloc)
Dernier hôte   : 192.168.63.254
Nombre d'hôtes : 2^12 − 2 = 4094
```

## 📝 À toi !

Remplis la carte d'identité de ces **3 réseaux** :

| | Réseau A | Réseau B | Réseau C |
|---|---|---|---|
| Adresse donnée | `192.168.1.75/24` | `192.168.10.100/26` | `172.16.37.10/20` |
| Difficulté | ⭐ | ⭐⭐ | ⭐⭐⭐ |

Pour chaque réseau (A, B, C), réponds aux questions **1 à 5** :

| N° | Information |
|---|---|
| **1** | Adresse réseau |
| **2** | Premier hôte |
| **3** | Broadcast |
| **4** | Dernier hôte |
| **5** | Nombre d'hôtes utilisables |

Exemple : `B3` = l'adresse de broadcast du réseau B.

📄 Réponds dans [`reponses.txt`](reponses.txt) puis vérifie :

```bash
python3 verifier.py 8
```

🏆 Si tu as 15/15, tu maîtrises les bases des masques réseau. Bravo !

---

➡️ Pour aller plus loin : [09 — Bonus : observer un vrai réseau](../09-bonus-observer-reseau/README.md)
