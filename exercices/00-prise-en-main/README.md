# Exercice 0 — Prise en main ⭐

⏱️ 5 minutes · 🎯 Objectif : apprendre à **répondre** et à **vérifier** ses réponses.

Cet exercice est très facile : il sert surtout à comprendre comment fonctionne l'atelier.

## Comment ça marche ?

Chaque exercice contient deux fichiers :

| Fichier | Rôle |
|---|---|
| `README.md` | L'énoncé (ce que tu lis en ce moment) |
| `reponses.txt` | Le fichier où tu **écris** tes réponses |

## Étape 1 — Ouvrir le fichier de réponses

Dans l'explorateur de fichiers (à gauche), ouvre `exercices/00-prise-en-main/reponses.txt`.

Tu vois des lignes comme :

```text
# Nombre de bits dans une adresse IPv4
Q1 = 
```

- Les lignes qui commencent par `#` sont des **commentaires** : elles rappellent la question.
- Tu écris ta réponse **après le signe `=`**.

## Étape 2 — Répondre

Réponds aux 3 questions (relis la partie 1 du [cours](../../Chapitre_Masques_Reseau_IPv4_Discord.md) si besoin) :

| Question | Énoncé |
|---|---|
| **Q1** | Combien de bits contient une adresse IPv4 ? |
| **Q2** | Combien de bits contient un octet ? |
| **Q3** | Combien d'octets contient une adresse IPv4 ? |

Exemple de ligne remplie : `Q1 = 12` (ce n'est pas la bonne réponse 😉).

Puis **enregistre** le fichier : `Ctrl + S` (ou `Cmd + S` sur Mac).

> 💡 Un point blanc ● sur l'onglet du fichier signifie qu'il **n'est pas enregistré**.

## Étape 3 — Vérifier

Dans le **terminal** (en bas de l'écran), tape puis appuie sur `Entrée` :

```bash
python3 verifier.py 0
```

Tu verras pour chaque question :

| Symbole | Signification |
|---|---|
| ✅ | Bonne réponse |
| ❌ | Mauvaise réponse → lis l'**indice** 💡 affiché |
| ⚠️ | Réponse mal écrite (par exemple des lettres au lieu d'un nombre) |
| ⬜ | Pas encore répondu |

Corrige, enregistre, relance… jusqu'à obtenir **3/3** 🎉

> 💡 Astuce : dans le terminal, la **flèche du haut ↑** rappelle la dernière commande tapée. Pratique pour relancer la vérification !

---

➡️ Exercice suivant : [01 — Du décimal au binaire](../01-binaire/README.md)
