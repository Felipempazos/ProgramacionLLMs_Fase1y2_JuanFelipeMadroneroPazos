import pandas as pd
import numpy as np
import random

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


def generar_caso_de_uso_analizar_confianza_lector():
    """
    Genera un caso de uso aleatorio para la función
    analizar_confianza_lector
    """

    n = random.randint(6, 12)

    data = []

    for _ in range(n):
        data.append({
            "num_paginas_leidas": random.uniform(0, 100),
            "frecuencia_lectura": random.uniform(0, 7),
            "nivel_comprension": random.uniform(0, 10),
            "habito": random.randint(0, 1)
        })

    df = pd.DataFrame(data)

    # asegurar ambas clases (evita error en LogisticRegression)
    df.loc[0, "habito"] = 0
    df.loc[1, "habito"] = 1

    input_data = {
        "df": df.copy()
    }

    # ---------------------------
    # OUTPUT esperado
    # ---------------------------
    df_calc = df.copy()

    X = df_calc[["num_paginas_leidas", "frecuencia_lectura", "nivel_comprension"]]
    y = df_calc["habito"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    modelo = LogisticRegression()
    modelo.fit(X_scaled, y)

    probs = modelo.predict_proba(X_scaled)
    max_probs = probs.max(axis=1)

    indices_baja_confianza = np.where(max_probs < 0.6)[0]

    output_data = indices_baja_confianza

    return input_data, output_data