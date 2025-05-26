# scripts/visualize_wind_data.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Cargar datos limpios
file_path = "Group4_data_analysis/data/noaa_wind_miami_cleaned.csv"
df = pd.read_csv(file_path)

# Asegurarse de que la fecha esté en formato datetime
df['date'] = pd.to_datetime(df['date'])

# Configurar estilo visual
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# 📈 1. Gráfica de líneas: evolución temporal
plt.figure()
sns.lineplot(x="date", y="value", data=df)
plt.title("Evolución de la velocidad del viento en Miami (2015-2023)")
plt.xlabel("Fecha")
plt.ylabel("Velocidad del viento (m/s)")
plt.tight_layout()
plt.savefig("Group4_data_analysis/data/plot_linea_evolucion.png")
print("✅ Gráfico de líneas guardado.")

# 📊 2. Histograma: distribución de velocidades
plt.figure()
sns.histplot(df["value"], bins=30, kde=True, color='skyblue')
plt.title("Distribución de la velocidad del viento (2015-2023)")
plt.xlabel("Velocidad del viento (m/s)")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.savefig("Group4_data_analysis/data/plot_histograma_distribucion.png")
print("✅ Histograma guardado.")

# 📅 3. Boxplot mensual: variación por mes
plt.figure()
df["month"] = df["date"].dt.month
sns.boxplot(x="month", y="value", data=df, palette="Set2")
plt.title("Distribución mensual de la velocidad del viento")
plt.xlabel("Mes")
plt.ylabel("Velocidad del viento (m/s)")
plt.tight_layout()
plt.savefig("Group4_data_analysis/data/plot_boxplot_mensual.png")
print("✅ Boxplot mensual guardado.")
