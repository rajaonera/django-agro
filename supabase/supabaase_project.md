

---

# Cahier d’activités — Jours 1 à 3

---

## Jour 1 — Analyse & conception / Mise en place Auth & BDD

### Objectifs :

* Comprendre les besoins fonctionnels et techniques
* Concevoir le modèle de données
* Mettre en place l’authentification Supabase

### Tâches :

1. **Analyse fonctionnelle rapide**

   * Lister précisément les données à gérer (users, lieux, météo, alertes)
   * Définir les relations entre ces entités

2. **Modélisation de la base de données**

   * Schéma des tables principales :

     * `users` (déjà gérée par Supabase Auth)
     * `locations` (lieux favoris avec coordonnées GPS)
     * `météo_realtime` (données météo récupérées)
     * `alertes` (alertes personnalisées liées aux utilisateurs)
   * Diagramme simple (ex: sur papier ou outil en ligne)

3. **Création des tables sur Supabase**

   * Créer les tables dans la console Supabase
   * Définir les clés primaires et étrangères

4. **Configurer l’authentification Supabase**

   * Activer l’auth email/mot de passe
   * Tester inscription et connexion via le dashboard Supabase

---

## Jour 2 — Intégration API météo & Edge Function de mise à jour

### Objectifs :

* Configurer la récupération des données météo
* Automatiser la mise à jour via Edge Function

### Tâches :

1. **Choisir une API météo externe** (ex : OpenWeatherMap)

   * Créer un compte si besoin et obtenir une clé API

2. **Créer une Edge Function dans Supabase**

   * Écrire un script qui :

     * Récupère les données météo pour les lieux stockés
     * Stocke ou met à jour ces données dans la table `météo_realtime`

3. **Tester la fonction manuellement**

   * Exécuter l’Edge Function depuis la console
   * Vérifier que les données météo sont bien insérées/actualisées

4. **Planifier la fonction (cron)**

   * Configurer l’exécution périodique (ex: toutes les heures)

---

## Jour 3 — Vues SQL & Fonctions de détection d’alertes

### Objectifs :

* Créer des vues pour simplifier l’accès aux données
* Développer des fonctions SQL pour détecter les alertes météo

### Tâches :

1. **Créer des vues SQL simples**

   * Vue pour lister la météo récente par utilisateur (lieux favoris)
   * Vue pour afficher les alertes actives

2. **Créer des vues matérialisées**

   * Par exemple, synthèse journalière des températures extrêmes ou pluies importantes

3. **Développer des fonctions SQL**

   * Fonctions détectant par exemple :

     * Température > seuil critique
     * Pluie ou vent fort prévu

4. **Tester ces vues et fonctions**

   * Exécuter les requêtes dans Supabase
   * Vérifier la pertinence des résultats

---
