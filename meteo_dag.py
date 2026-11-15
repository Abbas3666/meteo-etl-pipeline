from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import requests
import pandas as pd
import psycopg2

# --- LA FONCTION QUI FAIT LE TRAVAIL ---
def extraire_et_stocker():
    print("Début de l'extraction...")
    url = "https://api.open-meteo.com/v1/forecast?latitude=47.22&longitude=-1.55&current_weather=true"
    donnee = requests.get(url).json()
    
    meteo_propre = {
        "ville": "Nantes",
        "temperature": donnee["current_weather"]["temperature"],
        "vent": donnee["current_weather"]["windspeed"],
        "date": donnee["current_weather"]["time"]
    }
    
    # Connexion à PostgreSQL (Attention : on utilise "postgres" comme host, car on est dans Docker)
    conn = psycopg2.connect(
        host="postgres", # <-- C'est le nom du service dans Docker !
        port="5432",
        database="airflow", # <-- La base de données par défaut d'Airflow
        user="airflow",
        password="airflow"
    )
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS meteo (
            id SERIAL PRIMARY KEY,
            ville TEXT,
            temperature REAL,
            vent REAL,
            date TEXT
        )
    """)
    
    cur.execute("""
        INSERT INTO meteo (ville, temperature, vent, date) 
        VALUES (%s, %s, %s, %s)
    """, (meteo_propre["ville"], meteo_propre["temperature"], meteo_propre["vent"], meteo_propre["date"]))
    
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Données enregistrées !")

# --- LA CONFIGURATION DU DAG ---
# On dit à Airflow de lancer ça toutes les heures
default_args = {
    'owner': 'abbas',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'meteo_pipeline',
    default_args=default_args,
    description='Un pipeline qui récupère la météo toutes les heures',
    schedule_interval=timedelta(hours=1), # Toutes les heures
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['meteo', 'data'],
) as dag:

    # On crée la tâche
    tache_meteo = PythonOperator(
        task_id='recuperer_meteo',
        python_callable=extraire_et_stocker,
    )

    tache_meteo
