import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# 1. Se connecter à PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="meteo_db",
    user="admin",
    password="admin"
)

# 2. Lire les données
df = pd.read_sql("SELECT date, temperature FROM meteo ORDER BY date ASC", conn)
conn.close()

# 3. Tracer le graphique
df['date'] = pd.to_datetime(df['date'])
plt.figure(figsize=(10, 5))
plt.plot(df['date'], df['temperature'], marker='o', linestyle='-', color='blue')
plt.title('Évolution de la température à Nantes')
plt.xlabel('Date')
plt.ylabel('Température (°C)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('dashboard_meteo.png')  # sauvegarde en image
plt.show()
