# 🌐 Atelier — Les masques réseau IPv4

Bienvenue ! Dans cet atelier, tu vas **mettre en pratique** ce que tu as appris en cours sur les masques réseau, avec des exercices **progressifs** et **corrigés automatiquement**.

## 🎯 À la fin de l'atelier, tu sauras…

- convertir une adresse IP et un masque en **binaire** ;
- passer d'un masque décimal (`255.255.255.0`) à la notation **CIDR** (`/24`) ;
- utiliser l'opération **AND** pour trouver l'**adresse réseau** ;
- dire si deux machines sont sur le **même réseau** ou s'il faut passer par la **passerelle** ;
- calculer le **nombre de machines** d'un réseau et choisir le bon masque.

## 🚀 Pour commencer : 3 étapes

| Étape | Guide | Durée |
|---|---|---|
| 1 | [Créer un compte GitHub](guide/1-creer-compte-github.md) (si tu n'en as pas) | 10 min |
| 2 | [Créer ton dépôt à partir du template](guide/2-utiliser-le-template.md) | 5 min |
| 3 | [Travailler dans Codespace](guide/3-utiliser-codespace.md) | 10 min |

> 👀 Tu lis ce fichier **dans ton Codespace** ? Les étapes 1 à 3 sont faites, bravo ! Commence directement par l'exercice 0.

## 📝 Les exercices

Fais-les **dans l'ordre** : chacun s'appuie sur le précédent.

| N° | Exercice | Niveau | Durée |
|---|---|---|---|
| 0 | [Prise en main](exercices/00-prise-en-main/README.md) | ⭐ | 5 min |
| 1 | [Du décimal au binaire (un octet)](exercices/01-binaire/README.md) | ⭐ | 15 min |
| 2 | [Une adresse IP en binaire](exercices/02-ip-en-binaire/README.md) | ⭐ | 15 min |
| 3 | [Le masque : binaire et notation CIDR](exercices/03-masque-et-cidr/README.md) | ⭐⭐ | 20 min |
| 4 | [L'opération AND (ET logique)](exercices/04-operation-and/README.md) | ⭐⭐ | 15 min |
| 5 | [Trouver l'adresse réseau](exercices/05-adresse-reseau/README.md) | ⭐⭐ | 25 min |
| 6 | [Même réseau ? Direct ou passerelle ?](exercices/06-meme-reseau/README.md) | ⭐⭐ | 20 min |
| 7 | [Combien de machines ?](exercices/07-nombre-de-machines/README.md) | ⭐⭐ | 20 min |
| 8 | [Défi : la carte d'identité d'un réseau](exercices/08-defi-carte-reseau/README.md) | ⭐⭐⭐ | 30 min |
| 9 | [Bonus : observer un vrai réseau](exercices/09-bonus-observer-reseau/README.md) | ⭐⭐ | 15 min |
| 10 | [Bonus : programmer son calculateur (Python)](exercices/10-bonus-python/README.md) | ⭐⭐⭐ | 30-45 min |

## 🔁 La méthode pour chaque exercice

```text
1. Lire l'énoncé          →  exercices/XX-.../README.md
2. Écrire ses réponses    →  exercices/XX-.../reponses.txt   (puis Ctrl+S)
3. Vérifier               →  python3 verifier.py XX          (dans le terminal)
4. Corriger avec l'indice 💡 et recommencer jusqu'à 100 %
5. Enregistrer sur GitHub →  commit + push
```

Pour voir ta progression globale :

```bash
python3 verifier.py
```

## 🆘 Je suis bloqué(e)

1. Relis le **rappel** et l'**exemple résolu** en haut de l'énoncé.
2. Lis l'**indice** 💡 donné par le vérificateur.
3. Consulte l'[aide-mémoire](aide-memoire.md) ou le [cours complet](Chapitre_Masques_Reseau_IPv4_Discord.md).
4. Prends une feuille et un crayon : écrire le binaire à la main aide beaucoup !
5. Demande à ton voisin ou ta voisine… puis à ton enseignant·e 🙋
