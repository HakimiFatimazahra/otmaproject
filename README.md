# ✅ OTMAProject - Application Django de Validation de Checklists

OTMAProject est une application web développée avec Django pour la saisie et la validation de **fiches de contrôle (checklists)** liées à des machines de type Komax. Le projet propose une interface utilisateur avec gestion de rôles (`Saisisseur` et `Validateur`) permettant d'ajouter, consulter, valider ou refuser les fiches selon un statut.

---

## 🎯 Fonctionnalités principales

- 📝 **Saisie de fiches** avec des champs techniques (pressions, longueurs, mesures).
- ✅ **Validation ou refus** des fiches par un Validateur.
- 👥 **Deux types d'utilisateurs** :
  - `Saisisseur` : crée des fiches.
  - `Validateur` : consulte les fiches et change leur statut (`En attente`, `Valide`, `Non-Valide`).
- 🔒 Authentification des utilisateurs.
- - dashboard:Tableau de bord statistique
---

## 🧱 Technologies utilisées

- **Python 3.11**
- **Django 4.x**
- **Bootstrap 5** (pour le design)
- **Postgresql** (base de données )

---

## 📁 Structure du projet

```bash
otmaproject/
├── accounts/                # App de gestion des utilisateurs
├── omtaapp/                 # App principale : gestion des CheckLists
├── static/                  # Fichiers CSS/JS Bootstrap
├── templates/               # Templates HTML
├── db.postgresql              # Base de données
├── manage.py
├── .gitignore
└── README.md
