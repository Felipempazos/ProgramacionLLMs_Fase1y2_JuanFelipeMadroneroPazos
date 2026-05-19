import pandas as pd
import numpy as np

def identificar_rutas_criticas(df, percentil):
    df = df.copy()
    
    df['retraso'] = df['tiempo_real'] - df['tiempo_estimado']
    
    umbral_percentil = np.percentile(df['retraso'], percentil)
    
    df_filtrado = df[df['retraso'] > umbral_percentil]
    
    resultado = df_filtrado.sort_values(by='retraso', ascending=False)
    
    return resultado
