import os
import numpy as np
from src.data_preprocessing import load_data, preprocess_data
from src.model import create_model

# 🔄 Charger les données existantes
df = load_data('data/cac40_latest.csv')  # Assure-toi que ce chemin est bon
X, y, scaler = preprocess_data(df)

# 🧠 Mise en forme des données pour LSTM
X = X.reshape((X.shape[0], X.shape[1], 1))

# 🏗️ Création et entraînement du modèle
model = create_model((X.shape[1], 1))
model.fit(X, y, epochs=10, batch_size=32)

# 💾 Sauvegarde du modèle
os.makedirs('model', exist_ok=True)
model.save('model/cac40_lstm.h5')
print("✅ Modèle entraîné et sauvegardé")
