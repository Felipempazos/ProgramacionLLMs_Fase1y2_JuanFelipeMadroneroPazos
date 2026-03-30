import pandas as pd
import numpy as np
import random

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def generar_caso_de_uso_analizar_perfiles_musicales():
    """
    Genera un caso de uso aleatorio para la función
    analizar_perfiles_musicales
    """

    n = random.randint(5, 10)

    data = []

    for usuario in range(n):
        data.append({
            "usuario_id": usuario,
            "tiempo_pop": random.uniform(0, 100),
            "tiempo_rock": random.uniform(0, 100),
            "tiempo_reggaeton": random.uniform(0, 100)
        })

    df = pd.DataFrame(data)

    input_data = {
        "df": df.copy()
    }

    df_calc = df.copy()

    X = df_calc[["tiempo_pop", "tiempo_rock", "tiempo_reggaeton"]]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=2, random_state=0, n_init=10)
    clusters = kmeans.fit_predict(X_scaled)

    df_calc["cluster"] = clusters

    etiquetas_cluster = {}

    for cluster_id in np.unique(clusters):
        grupo = df_calc[df_calc["cluster"] == cluster_id]

        promedios = grupo[["tiempo_pop", "tiempo_rock", "tiempo_reggaeton"]].mean()

        max_val = promedios.max()
        min_val = promedios.min()

        # Umbral 20: si la diferencia entre el género más y menos escuchado
        # supera 20 minutos, el cluster es "especializado"; si no, "diverso"
        if max_val - min_val > 20:
            etiquetas_cluster[cluster_id] = "especializado"
        else:
            etiquetas_cluster[cluster_id] = "diverso"

    resultado = {}

    for _, row in df_calc.iterrows():
        resultado[int(row["usuario_id"])] = etiquetas_cluster[row["cluster"]]

    output_data = resultado

    return input_data, output_data
