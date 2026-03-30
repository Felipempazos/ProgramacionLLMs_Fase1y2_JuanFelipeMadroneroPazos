import pandas as pd
import numpy as np
import random


def generar_caso_de_uso_recomendar_estrategia_aprendizaje():
    """
    Genera un caso de uso aleatorio para la función
    recomendar_estrategia_aprendizaje
    """

    n_estudiantes = random.randint(3, 6)
    actividades = ['lectura', 'practica', 'video']

    filas = []

    for estudiante in range(n_estudiantes):
        n_registros = random.randint(3, 6)
        for _ in range(n_registros):
            filas.append({
                "estudiante_id": estudiante,
                "tipo_actividad": random.choice(actividades)
            })

    df = pd.DataFrame(filas)

    input_data = {
        "df": df.copy()
    }

    resultado = {}

    for estudiante_id, grupo in df.groupby("estudiante_id"):
        # mode()[0] devuelve la primera moda en orden alfabético en caso de empate
        # (lectura < practica < video), consistente con lo documentado en el enunciado
        actividad_dominante = grupo["tipo_actividad"].mode()[0]

        if actividad_dominante == "lectura":
            recomendacion = "reforzar con ejercicios prácticos"
        elif actividad_dominante == "practica":
            recomendacion = "reforzar con teoría"
        else:
            recomendacion = "combinar con actividades escritas"

        resultado[estudiante_id] = recomendacion

    output_data = resultado

    return input_data, output_data
