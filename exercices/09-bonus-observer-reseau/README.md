# Exercice 9 — Bonus : observer un vrai réseau ⭐⭐

⏱️ 15 minutes · 🎯 Objectif : retrouver les notions de l'atelier sur une **vraie machine** : ton Codespace !

Ton Codespace est un vrai ordinateur Linux, connecté à un vrai réseau. Il a donc une adresse IP et un masque.

## Étape 1 — Afficher l'adresse IP

Dans le terminal, tape :

```bash
ip -br -4 addr
```

> `ip` = outil réseau de Linux · `-br` = affichage court · `-4` = IPv4 seulement · `addr` = adresses

Tu obtiens quelque chose comme (tes valeurs seront sans doute différentes) :

```text
lo               UNKNOWN        127.0.0.1/8
eth0             UP             10.0.4.120/16
docker0          DOWN           172.17.0.1/16
```

Chaque ligne est une **interface réseau** (une « carte réseau ») :

- `lo` : l'interface **localhost** (tu as rencontré `127.0.0.1` à l'exercice 2 !) ;
- `eth0` : la carte réseau principale, **c'est celle qui nous intéresse** ;
- `docker0` : une interface virtuelle (on l'ignore).

👉 Remarque : la notation **CIDR** (`/16`, `/8`…) est utilisée directement par Linux !

## Étape 2 — Calculer à la main

À partir de la ligne `eth0`, remplis [`reponses.txt`](reponses.txt) :

| Question | Énoncé |
|---|---|
| **Q1** | L'adresse IP de `eth0` (sans le `/`) |
| **Q2** | Le CIDR de `eth0` (par exemple `/16`) |
| **Q3** | Le masque en décimal pointé |
| **Q4** | L'adresse réseau |
| **Q5** | Le nombre d'hôtes utilisables sur ce réseau |

Vérifie (le vérificateur calcule les bonnes réponses à partir de **ton** Q1 et **ton** Q2) :

```bash
python3 verifier.py 9
```

## Étape 3 — Vérifier avec la calculatrice

Une calculatrice qui **montre tous les calculs en binaire** est fournie. Essaie-la avec ton adresse, puis avec les adresses des exercices précédents :

```bash
python3 outils/calculatrice.py 192.168.50.50/20
```

> 🙏 Utilise-la pour **vérifier** ou **comprendre** une erreur, pas pour faire les exercices à ta place : le jour de l'examen, elle ne sera pas là !

## Étape 4 — Qui est ma passerelle ?

```bash
ip route
```

La ligne `default via X.X.X.X` indique l'adresse de la **passerelle** : c'est là que ton Codespace envoie tout ce qui n'est **pas sur son réseau** (par exemple github.com).

🧠 Question de réflexion (pas de vérification automatique) : la passerelle est-elle sur le même réseau que `eth0` ? Pourquoi est-ce **obligatoire** ?

---

➡️ Pour aller encore plus loin : [10 — Bonus : programmer son calculateur](../10-bonus-python/README.md)
