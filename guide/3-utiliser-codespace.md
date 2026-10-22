# Étape 3 — Travailler dans Codespace

⏱️ 10 minutes

## C'est quoi Codespace ?

**GitHub Codespaces** te donne un **ordinateur Linux dans ton navigateur**, avec l'éditeur **Visual Studio Code** déjà installé. Rien à installer sur ton PC !

## 1. Lancer ton Codespace

1. Sur la page de **ton** dépôt (`ton-nom/atelier-masques-reseau`), clique sur le bouton vert **`<> Code`**.
2. Choisis l'onglet **Codespaces**.
3. Clique sur **Create codespace on main**.
4. Patiente 1 à 2 minutes pendant la préparation ☕

## 2. Découvrir l'écran

```text
┌────┬───────────────────┬──────────────────────────────────┐
│ 📄 │  EXPLORATEUR      │  ÉDITEUR                         │
│ 🔍 │  (tes fichiers)   │  (le fichier ouvert)             │
│ 🔀 │                   │                                  │
│    │  ▸ exercices      │                                  │
│    │  ▸ guide          │                                  │
│    │  ▸ outils         │                                  │
│    │    README.md      ├──────────────────────────────────┤
│    │    verifier.py    │  TERMINAL                        │
│    │                   │  $ python3 verifier.py 0         │
└────┴───────────────────┴──────────────────────────────────┘
```

| Zone | À quoi elle sert |
|---|---|
| **Explorateur** (à gauche) | Voir et ouvrir les fichiers. Clique sur un dossier pour l'ouvrir. |
| **Éditeur** (au centre) | Lire les énoncés et écrire tes réponses. |
| **Terminal** (en bas) | Taper des commandes. S'il n'est pas visible : menu ☰ → **Terminal → New Terminal**, ou `Ctrl + ù` / `` Ctrl + ` ``. |
| **Contrôle de code source** 🔀 (barre de gauche) | Enregistrer ton travail sur GitHub (voir plus bas). |

> 💡 Les énoncés (`README.md`) s'ouvrent en mode **lecture**. Les fichiers `reponses.txt` s'ouvrent en mode **écriture**.

## 3. Les seules commandes à connaître

Tape-les dans le terminal puis appuie sur `Entrée` :

| Commande | Ce qu'elle fait |
|---|---|
| `python3 verifier.py` | Affiche ta **progression** sur tous les exercices |
| `python3 verifier.py 3` | **Vérifie** l'exercice 3 et donne des indices |
| `python3 outils/calculatrice.py 192.168.1.10/24` | Calculatrice qui montre le binaire (bonus) |
| `clear` | Efface le terminal |
| Flèche **↑** | Rappelle la commande précédente |

## 4. Enregistrer ton travail sur GitHub (commit + push) 💾

`Ctrl + S` enregistre le fichier **dans le Codespace**. Pour le sauvegarder **sur GitHub** (et ne jamais le perdre), il faut faire un **commit** puis un **push**. Fais-le à la fin de **chaque exercice**.

**Avec la souris (le plus simple) :**

1. Clique sur l'icône **Contrôle de code source** 🔀 dans la barre de gauche (un petit chiffre indique le nombre de fichiers modifiés).
2. Dans la zone **Message**, écris ce que tu as fait, par exemple : `Exercice 1 terminé`.
3. Clique sur la flèche à côté de **Commit** et choisis **Commit & Push** (ou clique sur **Commit** puis **Sync Changes**).
4. Si une fenêtre te demande s'il faut inclure tous les fichiers (*stage all changes*), réponds **Yes** / **Always**.

**Avec le terminal (pour les curieux) :**

```bash
git add .
git commit -m "Exercice 1 terminé"
git push
```

✅ Vérification : rafraîchis la page de ton dépôt sur github.com, ton message de commit apparaît en haut de la liste des fichiers.

## 5. Arrêter et reprendre

- **Reprendre plus tard** : va sur https://github.com/codespaces et clique sur ton Codespace. Tout est comme tu l'as laissé.
- **Arrêter** : le Codespace s'arrête tout seul après 30 minutes d'inactivité. Tu peux aussi l'arrêter depuis https://github.com/codespaces (menu `…` → **Stop codespace**).
- **Quota gratuit** : GitHub offre chaque mois un temps d'utilisation gratuit, largement suffisant pour cet atelier. Pense quand même à arrêter ton Codespace quand tu as fini.
- ⚠️ Un Codespace **inutilisé pendant 30 jours est supprimé**. C'est pour ça qu'il faut faire **commit + push** : ton travail reste alors en sécurité sur GitHub.

---

➡️ C'est parti : [Exercice 0 — Prise en main](../exercices/00-prise-en-main/README.md)
