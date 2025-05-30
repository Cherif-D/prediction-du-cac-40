import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import os
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def download_cac40(output_file='data/cac40_latest.csv'):
    """Télécharge les données CAC 40 et les sauvegarde."""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df = yf.download('^FCHI', start='2010-01-01')
    df.to_csv(output_file)
    return df

def load_data(filename='data/cac40_latest.csv'):
    """Charge les données CAC 40 depuis un fichier CSV."""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"❌ Le fichier {filename} est introuvable.")

    df = pd.read_csv(filename, encoding='utf-8-sig')
    df.columns = [col.strip() for col in df.columns]  # Nettoyage des noms de colonnes

    if 'Date' not in df.columns:
        raise ValueError(f"❌ La colonne 'Date' est introuvable dans le fichier {filename}. Colonnes trouvées : {df.columns.tolist()}")

    df.set_index('Date', inplace=True)
    df.index = pd.to_datetime(df.index)

    return df



def preprocess_data(df, window_size=60):
    """Transforme les données en séquences prêtes pour un modèle LSTM."""
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df[['Close']].values)

    X, y = [], []
    for i in range(window_size, len(scaled_data)):
        X.append(scaled_data[i-window_size:i])
        y.append(scaled_data[i])
    return np.array(X), np.array(y), scaler
