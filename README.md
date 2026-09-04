# 🌤️ Pourquoi j'ai fait ce projet météo ?

Salut ! Je m'appelle Abbas, je suis en Master Data IA , et je cherche une alternance en Data Engineering.

Ce petit projet, je l'ai fait pour **montrer concrètement** ce que je sais faire. Pas juste des mots sur un CV, mais du vrai code qui tourne.

---

## Le projet en 2 phrases

Je récupère la météo de Nantes en temps réel (via une API gratuite), je nettoie les données, je les stocke dans une base PostgreSQL, et je fais un petit graphique pour visualiser l'évolution des températures.

Rien de révolutionnaire, mais ça touche à tout ce qui est important pour un Data Engineer.

---

## Ce que j'ai utilisé

- **Python** (requests, pandas, matplotlib) – pour le traitement
- **PostgreSQL** – pour stocker les données
- **Docker** – pour lancer PostgreSQL sans l'installer sur ma machine
- **API Open-Meteo** – pour récupérer les données (gratuit, sans clé)
- **Git** – pour versionner mon code

---

## Comment j'ai fait concrètement

J'ai écrit un script Python qui :

1. Appelle l'API météo toutes les fois où je le lance
2. Transforme les données avec Pandas
3. Les insère dans PostgreSQL (qui tourne dans un conteneur Docker)

J'ai aussi fait un petit dashboard qui affiche l'évolution des températures sous forme de graphique.

---

## Ça ressemble à quoi ?

Voici ce que ça donne comme résultat :

![Dashboard météo](dashboard_meteo.png)

---

## Ce que j'aurais aimé faire en plus

Le projet est encore simple, mais il y a plein de choses que je pourrais ajouter :

- Lancer le script automatiquement toutes les heures (avec Airflow)
- Ajouter une alerte si la température dépasse 30°C
- Faire une petite interface web avec Streamlit
- Stocker les données dans le cloud (AWS)

Tout ça, c'est ce que j'apprendrai pendant mon alternance.

---

## Pourquoi ce projet ?

Parce que je voulais **mettre en pratique** ce que j'ai appris à l'université et en auto-formation.  
Parce qu'un recruteur qui voit du code sur GitHub, c'est plus parlant qu'un CV qui liste des compétences.

---

## Comment lancer le projet si tu veux tester

**1. Lancer PostgreSQL avec Docker**
```bash
docker run --name meteo-postgres -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -e POSTGRES_DB=meteo_db -p 5432:5432 -d postgres
