import requests
import pandas as pd
import psycopg2
from datetime import datetime

print(" Début du pipeline météo...")

# 1. Récupérer les données météo de Nantes via une API publique (gratuite, sans clé)
url = "https://api.open-meteo.com/v1/forecast?latitude=47.22&longitude=-1.55&current_weather=true"
response = requests.get(url)

# Vérifier que l'API a bien répondu
if response.status_code != 200:
    print("Erreur API :", response.status_code)
    exit()

data = response.json()
print(" Données récupérées avec succès")

# 2. Extraire les informations
meteo = {
    "ville": "Nantes",
    "temperature": data["current_weather"]["temperature"],
    "vent": data["current_weather"]["windspeed"],
    "direction_vent": data["current_weather"]["winddirection"],
    "date": data["current_weather"]["time"]
}

# 3. Créer un DataFrame Pandas (comme un tableau)
df = pd.DataFrame([meteo])
print(" Données récupérées :")
print(df)

# 4. Se connecter à PostgreSQL
try:
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="meteo_db",
        user="admin",
        password="admin"
    )
    cur = conn.cursor()
    print(" Connexion à PostgreSQL réussie")
except Exception as e:
    print("Erreur de connexion :", e)
    exit()

# 5. Créer la table (si elle n'existe pas)
cur.execute("""
    CREATE TABLE IF NOT EXISTS meteo (
        id SERIAL PRIMARY KEY,
        ville TEXT,
        temperature REAL,
        vent REAL,
        direction_vent REAL,
        date TEXT,
        date_insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()
print("Table vérifiée/créée")

# 6. Insérer les données
cur.execute("""
    INSERT INTO meteo (ville, temperature, vent, direction_vent, date)
    VALUES (%s, %s, %s, %s, %s)
""", (meteo["ville"], meteo["temperature"], meteo["vent"], meteo["direction_vent"], meteo["date"]))
conn.commit()

cur.close()
conn.close()

print(" Données météo stockées avec succès dans PostgreSQL !")
print(" Date :", meteo["date"])
print(" Température :", meteo["temperature"], "°C")
