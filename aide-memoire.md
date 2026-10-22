# 📌 Aide-mémoire — Masques réseau IPv4

## Poids des bits d'un octet

```text
128  64  32  16   8   4   2   1
```

## Valeurs possibles d'un octet de masque

| Binaire | Décimal | Bits à 1 |
|---|---|---|
| `00000000` | 0 | 0 |
| `10000000` | 128 | 1 |
| `11000000` | 192 | 2 |
| `11100000` | 224 | 3 |
| `11110000` | 240 | 4 |
| `11111000` | 248 | 5 |
| `11111100` | 252 | 6 |
| `11111110` | 254 | 7 |
| `11111111` | 255 | 8 |

## Opération AND

```text
0 AND 0 = 0      1 AND 0 = 0
0 AND 1 = 0      1 AND 1 = 1

X AND 255 = X    (on recopie)
X AND 0   = 0    (on efface)
```

## Formules

```text
Adresse réseau     = IP AND masque              (bits hôtes à 0)
Broadcast          = bits hôtes à 1
Premier hôte       = adresse réseau + 1
Dernier hôte       = broadcast − 1

Bits hôtes         = 32 − CIDR
Nombre d'adresses  = 2 ^ (bits hôtes)
Hôtes utilisables  = 2 ^ (bits hôtes) − 2
Taille du bloc     = 256 − octet « intéressant » du masque
```

## Tableau des masques courants

| CIDR | Masque | Bits hôtes | Adresses | Hôtes utilisables |
|---|---|---|---|---|
| /8 | 255.0.0.0 | 24 | 16 777 216 | 16 777 214 |
| /16 | 255.255.0.0 | 16 | 65 536 | 65 534 |
| /20 | 255.255.240.0 | 12 | 4 096 | 4 094 |
| /21 | 255.255.248.0 | 11 | 2 048 | 2 046 |
| /22 | 255.255.252.0 | 10 | 1 024 | 1 022 |
| /23 | 255.255.254.0 | 9 | 512 | 510 |
| /24 | 255.255.255.0 | 8 | 256 | 254 |
| /25 | 255.255.255.128 | 7 | 128 | 126 |
| /26 | 255.255.255.192 | 6 | 64 | 62 |
| /27 | 255.255.255.224 | 5 | 32 | 30 |
| /28 | 255.255.255.240 | 4 | 16 | 14 |
| /29 | 255.255.255.248 | 3 | 8 | 6 |
| /30 | 255.255.255.252 | 2 | 4 | 2 |

## Même réseau ?

```text
réseau(A) == réseau(B) ?   →  OUI : envoi direct
                           →  NON : envoi à la passerelle
```
