# Documentation du projet de convertisseurs

Ce projet contient plusieurs convertisseurs numériques développés par différents auteurs (Enzo, Erwan, Nolan), et un script principal qui permet de les lancer via une interface utilisateur simple.

## Structure du projet

```
sources/
│
├── main.py
└── convertisseurs/
    ├── ConvertisseurEnzo.py
    ├── ConvertisseurErwan.py
    └── ConvertisseurNolan.py
```

---

## `main.py`

### Description

Script principal de l'application. Il s'agit d'une interface utilisateur simple (via `tkinter`) qui permet de choisir entre les différents convertisseurs développés.

### Imports

- `subprocess` : pour lancer les autres scripts Python.
- `tkinter` : pour l’interface graphique principale.

### Fonctions principales

- `ouvrir_convertisseur_enzo()` : lance le convertisseur d’Enzo.
- `ouvrir_convertisseur_nolan()` : lance le convertisseur de Nolan.
- `ouvrir_convertisseur_erwan()` : lance le convertisseur d’Erwan.

---

## `convertisseurs/ConvertisseurEnzo.py`

### Description

Convertisseur numérique développé par Enzo. Permet de faire des conversions entre différentes bases (décimal, binaire, hexadécimal).

### Imports

- `tkinter` : interface utilisateur.
- `subprocess` : retour à l’accueil via `main.py`.

### Fonctions principales

- `binEnDeci(number)`
- `hexEnDeci(number)`
- `DeciEnHexa(nombre)`
- `DeciEnBin(nombres)`
- `bin_hex(entry)`
- `hex_bin(entry)`
- Interface utilisateur avec des événements (`valider_entree`, `fermer_fenetre`).

---

## `convertisseurs/ConvertisseurErwan.py`

### Description

Convertisseur numérique développé par Erwan. Très complet, avec des contrôles de saisie, une interface stylisée, et la possibilité de copier le résultat dans le presse-papier.

### Imports

- `tkinter`, `ttk`, `tkFont` : interface graphique enrichie.
- `clipboard` : pour copier le résultat.
- `subprocess` : navigation retour.

### Fonctions principales

- `dec_hex`, `dec_bin`, `bin_dec`, `hex_dec`, `bin_hex`, `hex_bin`
- Fonctions de gestion d’interface : `OnValidate`, `CopySortie`, `keypress`, `OnChoose`

---

## `convertisseurs/ConvertisseurNolan.py`

### Description

Convertisseur développé par Nolan. Plus orienté objet avec des classes pour structurer l'interface et la logique de conversion.

### Imports

- `tkinter` : pour l'interface graphique.
- `subprocess` : pour revenir au menu principal.

### Classes

- `Application` : classe principale de l’interface.
- `ConverterSide` : permet d’avoir des côtés convertibles indépendants (peut-être deux zones interactives).

### Fonctions principales

- `convert_between_bases(value, source_base, target_base)`
- Fonctions similaires aux autres convertisseurs : `binEnDeci`, `hexEnDeci`, `DeciEnHexa`, `DeciEnBin`, etc.

---

## Lien entre les fichiers

- **`main.py`** agit comme **menu principal**. Il appelle les autres fichiers via `subprocess` pour ouvrir leur interface respective.
- Les convertisseurs sont **autonomes**, chacun avec leur propre interface et logique de conversion, mais suivent un schéma similaire (conversion entre bases numériques, interface graphique avec `tkinter`, retour à l'accueil).
