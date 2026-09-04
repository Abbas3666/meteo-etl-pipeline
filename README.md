# 🌤️ Pipeline ETL Météo

## 📌 Objectif
Récupérer les données météo de Nantes via une API publique, les transformer avec Pandas, et les stocker dans PostgreSQL.

## 🛠️ Technologies utilisées
- **Python** : requests, pandas, matplotlib, psycopg2
- **PostgreSQL** : base de données (via Docker)
- **Docker** : conteneurisation de PostgreSQL
- **API** : Open-Meteo (gratuite, sans clé)
- **Git/GitHub** : versionnement

## ⚙️ Fonctionnalités
- ✅ Extraction des données météo en temps réel via API REST
- ✅ Nettoyage et structuration avec Pandas
- ✅ Stockage dans PostgreSQL avec Docker
- ✅ Dashboard de visualisation avec Matplotlib
- ✅ Pipeline ETL complet

## 🚀 Installation et exécution

### 1. Lancer PostgreSQL avec Docker
```bash
docker run --name meteo-postgres -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -e POSTGRES_DB=meteo_db -p 5432:5432 -d postgres
