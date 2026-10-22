# 🌐 Chapitre — Comprendre les masques réseau IPv4

> Version Markdown optimisée pour être copiée dans une discussion Discord.

\---

## 1️⃣ Pourquoi avons-nous besoin d’un masque réseau ?

Une adresse IPv4 permet d’identifier une interface réseau.

Exemple :

```text
192.168.50.50
```

Une adresse IPv4 est composée de **32 bits**, regroupés en **4 octets de 8 bits**.

```text
192      .168      .50       .50
8 bits    8 bits    8 bits    8 bits
```

Mais une adresse IP seule ne suffit pas.

Une machine doit aussi savoir :

* quelle partie de l’adresse correspond au **réseau** ;
* quelle partie correspond à la **machine**.

C’est le rôle du **masque de sous-réseau**.

💡 Le masque permet notamment à une machine de déterminer si une destination est située sur son réseau local ou si elle doit envoyer les données vers un routeur.

\---

## 2️⃣ Une adresse IPv4 contient 32 bits

Prenons l’adresse :

```text
192.168.50.50
```

En binaire :

```text
192 = 11000000
168 = 10101000
 50 = 00110010
 50 = 00110010
```

Donc :

```text
192.168.50.50

11000000.10101000.00110010.00110010
```

Chaque octet utilise 8 bits :

```text
┌──────────┬──────────┬──────────┬──────────┐
│   192    │   168    │    50    │    50    │
├──────────┼──────────┼──────────┼──────────┤
│11000000  │10101000  │00110010  │00110010  │
└──────────┴──────────┴──────────┴──────────┘
     8          8          8          8
```

Total :

```text
8 + 8 + 8 + 8 = 32 bits
```

\---

## 3️⃣ Une adresse contient deux informations

Une adresse IPv4 est composée de deux parties :

```text
┌──────────────────────┬─────────────────────┐
│     Partie réseau    │   Partie machine    │
│      Network ID      │       Host ID       │
└──────────────────────┴─────────────────────┘
```

Mais où se trouve la séparation ?

Par exemple :

```text
192.168.50.50
```

Doit-on lire :

```text
192.168.50 | 50
```

ou :

```text
192.168 | 50.50
```

ou encore couper au milieu d’un octet ?

👉 Impossible de le savoir avec l’adresse IP seule.

Il faut connaître le **masque réseau**.

Exemple :

```text
Adresse IP : 192.168.50.50
Masque     : 255.255.255.0
```

Le masque indique quels bits appartiennent au réseau et quels bits appartiennent aux machines.

\---

## 4️⃣ Comprendre le masque

Prenons :

```text
255.255.255.0
```

En binaire :

```text
11111111.11111111.11111111.00000000
```

La règle est simple :

```text
1 = partie réseau
0 = partie machine
```

Donc :

```text
11111111.11111111.11111111 | 00000000
──────── Partie réseau ──────|─ Hôte ─
```

Pourquoi `255` ?

Les poids d’un octet sont :

```text
128 64 32 16 8 4 2 1
```

Si tous les bits valent 1 :

```text
128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = 255
```

Donc :

```text
11111111 = 255
00000000 = 0
```

Quelques valeurs importantes :

```text
10000000 = 128
11000000 = 192
11100000 = 224
11110000 = 240
11111000 = 248
11111100 = 252
11111110 = 254
11111111 = 255
```

\---

## 5️⃣ L’opération AND

Pour trouver l’adresse réseau d’une machine, on utilise une opération logique :

```text
AND
```

ou **ET logique**.

Table de vérité :

```text
0 AND 0 = 0
0 AND 1 = 0
1 AND 0 = 0
1 AND 1 = 1
```

👉 Pour obtenir `1`, les deux bits doivent donc être à `1`.

Prenons :

```text
IP     : 192.168.50.50
Masque : 255.255.255.0
```

En binaire :

```text
  11000000.10101000.00110010.00110010
AND
  11111111.11111111.11111111.00000000
------------------------------------------------
  11000000.10101000.00110010.00000000
```

Résultat :

```text
192.168.50.0
```

Donc :

```text
IP AND masque = adresse réseau
```

Ici :

```text
192.168.50.50
AND 255.255.255.0
=
192.168.50.0
```

\---

## 6️⃣ Comment une machine utilise-t-elle le masque ?

Prenons deux machines :

```text
PC A : 192.168.50.10
PC B : 192.168.50.80

Masque : 255.255.255.0
```

Pour A :

```text
192.168.50.10
AND
255.255.255.0

= 192.168.50.0
```

Pour B :

```text
192.168.50.80
AND
255.255.255.0

= 192.168.50.0
```

Les deux résultats sont identiques :

```text
192.168.50.0 = 192.168.50.0
```

✅ A et B appartiennent donc au même réseau IP.

Maintenant :

```text
PC C : 192.168.51.20
```

Son réseau est :

```text
192.168.51.0
```

Donc :

```text
192.168.50.0 ≠ 192.168.51.0
```

A et C sont sur des réseaux différents.

➡️ Pour communiquer, ils devront passer par un **routeur / une passerelle**.

\---

## 7️⃣ La notation CIDR

Au lieu d’écrire :

```text
255.255.255.0
```

on peut écrire :

```text
/24
```

Pourquoi `/24` ?

Parce que le masque contient **24 bits à 1** :

```text
11111111.11111111.11111111.00000000
```

Soit :

```text
8 + 8 + 8 = 24
```

Donc :

```text
255.255.255.0 = /24
```

Exemples :

```text
/24 = 255.255.255.0
/23 = 255.255.254.0
/22 = 255.255.252.0
/21 = 255.255.248.0
/20 = 255.255.240.0
```

Plus le nombre après `/` diminue, plus on laisse de bits disponibles pour les machines.

```text
/24 → 8 bits hôtes
/23 → 9 bits hôtes
/22 → 10 bits hôtes
/20 → 12 bits hôtes
```

\---

## 8️⃣ Combien de machines peut contenir un réseau ?

La formule est :

```text
Nombre d’adresses = 2^(nombre de bits hôtes)
```

Exemple avec `/24` :

```text
32 - 24 = 8 bits hôtes

2⁸ = 256 adresses
```

Dans un sous-réseau IPv4 classique :

```text
256 - 2 = 254 hôtes utilisables
```

Deux adresses sont réservées :

```text
1 adresse réseau
1 adresse broadcast
```

Quelques valeurs à retenir :

```text
/24 → 256 adresses  → 254 hôtes
/23 → 512 adresses  → 510 hôtes
/22 → 1024 adresses → 1022 hôtes
/21 → 2048 adresses → 2046 hôtes
/20 → 4096 adresses → 4094 hôtes
```

Exemple : nous devons connecter **300 machines**.

```text
/24 → 254 hôtes ❌
/23 → 510 hôtes ✅
```

Le `/23` est donc suffisant.

\---

## 9️⃣ Attention : la séparation peut se faire au milieu d’un octet

Avec :

```text
255.255.255.0
```

la séparation réseau/machine tombe exactement entre deux octets :

```text
192 . 168 . 50 | 50
───────────────|────
    réseau      hôte
```

Mais ce n’est pas toujours le cas.

Prenons :

```text
255.255.240.0
```

En binaire :

```text
11111111.11111111.11110000.00000000
```

Il comporte :

```text
8 + 8 + 4 = 20 bits réseau
```

Il s’agit donc d’un :

```text
/20
```

La frontière passe au milieu du troisième octet :

```text
11111111.11111111.1111|0000.00000000
                       ↑
                   frontière
```

C’est pour cette raison qu’il est important de comprendre le binaire : la séparation entre réseau et machine ne correspond pas toujours à la séparation visuelle entre les nombres décimaux.

\---

## 🔟 Exemple : `192.168.50.50/20`

Prenons :

```text
192.168.50.50/20
```

Le masque est :

```text
255.255.240.0
```

En binaire :

```text
IP
11000000.10101000.00110010.00110010

MASQUE
11111111.11111111.11110000.00000000
```

Effectuons le AND :

```text
  11000000.10101000.00110010.00110010
AND
  11111111.11111111.11110000.00000000
------------------------------------------------
  11000000.10101000.00110000.00000000
```

Le troisième octet obtenu est :

```text
00110000 = 48
```

L’adresse réseau est donc :

```text
192.168.48.0/20
```

et non `192.168.50.0`.

Ce réseau va de :

```text
Adresse réseau : 192.168.48.0
Premier hôte   : 192.168.48.1
Dernier hôte   : 192.168.63.254
Broadcast      : 192.168.63.255
```

Il contient :

```text
4096 adresses
4094 hôtes utilisables
```

\---

## 🎯 Synthèse

```text
Adresse IPv4 = 32 bits
```

Le masque indique :

```text
1 = réseau
0 = machine
```

Pour trouver l’adresse réseau :

```text
Adresse IP
    AND
Masque réseau
     ↓
Adresse réseau
```

Une machine compare ensuite le réseau de sa propre adresse avec celui de la destination :

```text
              Même réseau ?
                /      \\
              OUI      NON
               │        │
        Communication   Envoi vers
            locale      la passerelle
```

Enfin :

```text
/24 = 24 bits réseau + 8 bits hôtes
/23 = 23 bits réseau + 9 bits hôtes
/22 = 22 bits réseau + 10 bits hôtes
/20 = 20 bits réseau + 12 bits hôtes
```

👉 **Chaque bit supplémentaire attribué à la partie hôte double le nombre d’adresses disponibles.**

\---

## 📌 À retenir

**Adresse IP seule : insuffisante.**

Il faut connaître le **masque** pour savoir :

* quel est le réseau ;
* quelle partie identifie la machine ;
* si une destination est locale ou distante ;
* si le paquet doit être envoyé directement ou vers une passerelle.

**Prochaine étape : le subnetting**

Nous verrons comment calculer pour un réseau donné :

```text
- l’adresse réseau ;
- la première adresse utilisable ;
- la dernière adresse utilisable ;
- l’adresse de broadcast ;
- le nombre d’hôtes disponibles.
```

Exemples à venir :

```text
/25
/26
/27
/28
...
```

