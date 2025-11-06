# preprocesamiento.py
import pandas as pd

def cargar_datos(ruta):
    """Carga un dataset desde un archivo CSV."""
    return pd.read_csv(ruta)

def limpiar_datos(df):
    """Elimina valores nulos y duplicados."""
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def normalizar_datos(df):
    """Normaliza columnas numéricas entre 0 y 1."""
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    df[df.select_dtypes(include=['float64', 'int64']).columns] = scaler.fit_transform(
        df.select_dtypes(include=['float64', 'int64'])
    )
    return df

if __name__ == "__main__":
    print("Funciones de preprocesamiento listas para usar.")
