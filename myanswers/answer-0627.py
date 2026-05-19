import pandas as pd

def normalizar_datos_legados(datos=None, registros=None):
    if datos is None:
        datos = {'registros': registros}
    
    df = datos['registros'].copy()
    
    df['fecha_raw'] = pd.to_datetime(df['fecha_raw'], format='%Y%m%d')
    
    mapa_estados = {1: 'Activo', 2: 'Inactivo', 3: 'Pendiente'}
    df['estado_desc'] = df['cod_estado'].map(mapa_estados).fillna('Error')
    
    df = df.drop(columns=['cod_estado'])
    
    return df