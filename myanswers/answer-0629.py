import pandas as pd

def analizar_cuello_botella(df_tiempos, tiempo_ciclo_max):
    df = df_tiempos.copy()
    
    df_filtrado = df[df['tiempo_operacion_seg'] > tiempo_ciclo_max].copy()
    df_filtrado['exceso_tiempo'] = df_filtrado['tiempo_operacion_seg'] - tiempo_ciclo_max
    
    resultado = df_filtrado[['estacion', 'exceso_tiempo']].sort_values(
        by='exceso_tiempo', ascending=False
    )
    
    return resultado
