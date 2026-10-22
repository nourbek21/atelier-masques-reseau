# 👩‍🏫 Guide enseignant

## Préparer le dépôt modèle (une seule fois)

1. Sur la page de ce dépôt GitHub : **Settings** → onglet **General**.
2. Coche la case **Template repository** (juste sous le nom du dépôt).
3. Vérifie que le dépôt est **public** (ou que tes étudiants y ont accès).
4. Communique le lien du dépôt aux étudiants.

Le bouton vert **Use this template** apparaît alors sur la page du dépôt.

> 💡 Conseil : teste toi-même le parcours complet (template → Codespace → `python3 verifier.py 0`) avec un second compte avant la séance.

## Avant la séance

- Demande aux étudiants de **créer leur compte GitHub à l'avance** : la vérification par e-mail et la double authentification peuvent prendre du temps (et les mails tombent parfois dans les spams).
- Un Codespace est prêt en 1 à 2 minutes. Le quota gratuit mensuel de GitHub suffit largement pour l'atelier.

## Déroulé conseillé (≈ 3 h)

| Temps | Activité |
|---|---|
| 0:00 – 0:25 | Guides 1 à 3 : compte, template, Codespace (en démonstration au vidéoprojecteur) |
| 0:25 – 0:30 | Exercice 0 tous ensemble : remplir `reponses.txt`, `Ctrl+S`, lancer le vérificateur |
| 0:30 – 1:20 | Exercices 1 à 4 (binaire, IP, masque/CIDR, AND) |
| 1:20 – 1:30 | Pause |
| 1:30 – 2:40 | Exercices 5 à 8 (adresse réseau, même réseau, nombre d'hôtes, défi) |
| 2:40 – 3:00 | Correction collective du défi (ex. 8) et/ou bonus 9 et 10 pour les plus rapides |

Points de vigilance fréquents :

- oubli de `Ctrl+S` avant de lancer le vérificateur ;
- terminal fermé (menu ☰ → Terminal → New Terminal) ;
- octet écrit sur moins de 8 bits (le vérificateur le signale) ;
- confusion « Open in a codespace » sur le **template** au lieu de « Create a new repository » : le travail n'est alors pas sauvegardé dans un dépôt de l'étudiant.

## Suivre la progression

Chaque étudiant peut afficher son bilan avec `python3 verifier.py`.
Pour consulter le travail d'un étudiant : il te transmet l'URL de son dépôt (s'il est privé, il doit t'ajouter comme collaborateur). Tu peux alors le cloner et lancer `python3 verifier.py`.

## Fonctionnement du vérificateur

- Les réponses attendues sont stockées **hachées** (SHA-256) dans `outils/attendu.json` : elles ne sont pas lisibles en clair.
- Plusieurs écritures sont acceptées : `/24` ou `24`, `oui`/`o`/`non`/`n`, `passerelle`/`routeur`, espaces ignorés.
- L'exercice 9 est vérifié par calcul à partir de l'adresse réelle du Codespace de l'étudiant.
- L'exercice 10 exécute les fonctions Python de l'étudiant sur des cas de test.

Le **corrigé** et le **script de génération** des réponses ne sont volontairement **pas** dans ce dépôt (les étudiants le copient). Conserve-les dans un dépôt privé.

## Suite

Le cours annonce le **subnetting** (/25, /26, /27…) comme prochaine étape : l'exercice 8 (réseau B en /26) et la notion de « taille du bloc » y préparent directement.
