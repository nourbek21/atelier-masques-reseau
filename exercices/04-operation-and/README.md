# Exercice 4 — L'opération AND (ET logique) ⭐⭐

⏱️ 15 minutes · 🎯 Objectif : maîtriser l'opération qui permet de trouver l'adresse réseau.

## 📖 Rappel : table de vérité

```text
0 AND 0 = 0
0 AND 1 = 0
1 AND 0 = 0
1 AND 1 = 1
```

👉 Le résultat vaut `1` **seulement si les deux bits valent 1**.

## ✍️ Exemple résolu : 10110110 AND 11110000

On aligne les bits et on traite **colonne par colonne** :

```text
    1 0 1 1 0 1 1 0
AND 1 1 1 1 0 0 0 0
    ---------------
    1 0 1 1 0 0 0 0
```

Résultat : `10110000`

> 🧠 **À remarquer** : là où le masque a des `1`, on **recopie** le bit du haut. Là où le masque a des `0`, on obtient **0**. Le masque agit comme un **filtre**.

## ✍️ Exemple résolu en décimal : 50 AND 240

On passe par le binaire :

```text
     50 = 0 0 1 1 0 0 1 0
AND 240 = 1 1 1 1 0 0 0 0
          ---------------
          0 0 1 1 0 0 0 0  = 48
```

## 📝 À toi !

| Question | Calculer |
|---|---|
| **Q1** | `1 AND 0` |
| **Q2** | `1 AND 1` |
| **Q3** | `11001100 AND 11110000` (réponse en binaire, 8 bits) |
| **Q4** | `00110010 AND 11110000` (réponse en binaire, 8 bits) |
| **Q5** | `50 AND 255` (réponse en décimal) |
| **Q6** | `50 AND 0` (réponse en décimal) |
| **Q7** | `200 AND 192` (réponse en décimal) |
| **Q8** | `77 AND 240` (réponse en décimal) |

📄 Réponds dans [`reponses.txt`](reponses.txt) puis vérifie :

```bash
python3 verifier.py 4
```

> 🧠 Après Q5 et Q6, tu devrais avoir découvert deux **raccourcis** très utiles :
> `X AND 255 = ?` et `X AND 0 = ?`

---

➡️ Exercice suivant : [05 — Trouver l'adresse réseau](../05-adresse-reseau/README.md)
