import os
import numpy as np
from tensorflow.keras.models import load_model
from src.data_preprocessing import load_data, preprocess_data

def predict_next_close():
    # 📁 Déterminer la racine du projet dynamiquement
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 📄 Chemins absolus des fichiers
    data_path = os.path.join(base_dir, 'data', 'cac40_latest.csv')
    model_path = os.path.join(base_dir, 'model', 'cac40_lstm.h5')

    # 🔄 Chargement des données
    df = load_data(data_path)

    # 🧹 Prétraitement
    X, y, scaler = preprocess_data(df)

    # 📅 Dernière date des données
    last_date = df.index[-1]