import pandas as pd
import numpy as np
import random


def generar_caso_de_uso_reconstruir_velocidad_faltante():
    """
    Genera un caso de uso aleatorio para la función
    reconstruir_velocidad_faltante
    """

    n = random.randint(5, 10)

    tiempo = np.arange(n)
    posicion = np.cumsum(np.random.uniform(1, 10, size=n))

    velocidad_real = posicion.copy()
    velocidad_real[1:] = posicion[1:] - posicion[:-1]
    velocidad_real[0] = 0

    velocidad = velocidad_real + np.random.uniform(-1, 1, size=n)

    # introducir NaN
    for i in range(n):
        if random.random() < 0.3:
            velocidad[i] = np.nan

    df = pd.DataFrame({
        "tiempo": tiempo,
        "posicion": posicion,
        "velocidad": velocidad
    })

    input_data = {
        "df": df.copy()
    }

    df_calc = df.copy()

    # Velocidad estimada por diferencia de posición; primer valor = 0
    velocidad_estimada = df_calc["posicion"].diff()
    velocidad_estimada.iloc[0] = 0

    # Rellenar NaN con la velocidad estimada
    df_calc["velocidad"] = df_calc["velocidad"].fillna(velocidad_estimada)

    # Error respecto a la velocidad ORIGINAL (antes del fillna)
    # donde la velocidad original era NaN, el error se trata como 0
    error = np.abs(velocidad_estimada - df["velocidad"])
    error = error.fillna(0)

    # Índices cuyo error supera el promedio (promedio incluye los ceros)
    umbral = error.mean()
    indices_error = np.where(error > umbral)[0]

    output_data = {
        "df_corregido": df_calc,
        "indices_error": indices_error
    }

    return input_data, output_data
