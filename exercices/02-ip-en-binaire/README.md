# Exercice 2 — Une adresse IP en binaire ⭐

⏱️ 15 minutes · 🎯 Objectif : écrire une adresse IPv4 complète (32 bits) en binaire.

## 📖 Rappel

Une adresse IPv4 = **4 octets** séparés par des points. On convertit **chaque octet séparément**, exactement comme dans l'exercice 1.

## ✍️ Exemple résolu : 192.168.50.50

```text
┌──────────┬──────────┬──────────┬──────────┐
│   192    │   168    │    50    │    50    │
├──────────┼──────────┼──────────┼──────────┤
│ 11000000 │ 10101000 │ 00110010 │ 00110010 │
└──────────┴──────────┴──────────┴──────────┘
```

Résultat : `11000000.10101000.00110010.00110010`

## 📝 À toi !

Format attendu pour le binaire : **4 groupes de 8 bits séparés par des points**.

| Question | Énoncé |
|---|---|
| **Q1** | Écris `10.0.0.1` en binaire |
| **Q2** | Écris `172.16.5.200` en binaire |
| **Q3** | Écris `11000000.10101000.00000001.00001010` en décimal |
| **Q4** | Écris `01111111.00000000.00000000.00000001` en décimal |

📄 Réponds dans [`reponses.txt`](reponses.txt) puis vérifie :

```bash
python3 verifier.py 2
```

> 🤓 **Le savais-tu ?** L'adresse de Q4 est spéciale : c'est l'adresse **localhost**, qui désigne « ma propre machine ».

---

➡️ Exercice suivant : [03 — Le masque et la notation CIDR](../03-masque-et-cidr/README.md)
