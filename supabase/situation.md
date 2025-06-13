# 11 - 06 - 25
---

## 🔐 Projet : **Système d’authentification web avec Supabase**

### 🎯 Objectif

Développer une **interface web simple** qui permet aux utilisateurs de :

* S’inscrire avec email + mot de passe
* Se connecter avec mot de passe
* Se connecter par **lien magique** (magic link envoyé par mail)
* Voir les informations de session
* Se déconnecter

---

### 🧰 Technologies utilisées

* **Frontend** : HTML, JavaScript
* **Backend/Auth** : [Supabase](https://supabase.com) (base de données PostgreSQL + service Auth intégré)
* **Librairie JS** : `@supabase/supabase-js`

---

### ⚙️ Fonctionnalités implémentées

* Formulaire d’inscription (`signUp`)
* Formulaire de connexion classique (`signIn`)
* Connexion via lien magique (`sendMagicLink`)
* Récupération de l’utilisateur courant (`getUser`)
* Déconnexion (`signOut`)
* Redirection vers `dashboard.html` après connexion

---

### 🐞 Problèmes rencontrés et résolus

* **Initialisation de Supabase trop tardive dans le script** → corrigé en plaçant la création du client **hors du DOMContentLoaded**
* **Fonction `signUp` non définie** → corrigé en déclarant proprement la fonction dans la portée globale
* **Emails de vérification non reçus** → lié à une **configuration SMTP manquante** dans Supabase

---

### ✅ Prochaine étape indispensable

👉 **Configurer les paramètres SMTP** dans Supabase pour permettre :

* L’envoi d’emails de confirmation d’inscription
* Le fonctionnement des liens magiques
* Les demandes de réinitialisation de mot de passe

---

### 🛠️ Évolutions futures possibles

* Ajouter la **validation de formulaire** (email valide, mots de passe forts)
* Ajouter une interface de profil utilisateur
* Intégrer Supabase Auth avec une base de données d’utilisateurs personnalisée
* Utiliser **Edge Functions** pour des règles de sécurité supplémentaires

# 12 06 25 