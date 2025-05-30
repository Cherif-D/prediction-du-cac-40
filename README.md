# 📈 Prédiction quotidienne du CAC 40 avec LSTM et Streamlit

Bienvenue dans ce projet personnel de **prédiction journalière de l'indice boursier français CAC 40**, réalisé en **autonomie** par **Diallo Mamadou Cherif**. Ce projet combine **Deep Learning**, **traitement de séries temporelles**, et **interface web interactive** via **Streamlit**.

---

## 🎯 Objectif du projet

L’objectif principal est de concevoir une application capable de :

- Prédire la **valeur de clôture du CAC 40** à l'aide d'un modèle LSTM entraîné sur données historiques,
- Visualiser l'évolution du marché via un **graphique interactif**,
- Offrir une interface utilisateur accessible et intuitive avec **Streamlit**,
- Automatiser le pipeline complet : **téléchargement des données**, **prétraitement**, **entraînement**, **prédiction**, et **visualisation**.

---

## 📊 Choix du dataset

Les données proviennent de la source libre **Yahoo Finance** (`yfinance`) et concernent :

- L’indice CAC 40 (`^FCHI`) depuis 2010,
- Colonnes utilisées : `Close`, `Open`, `High`, `Low`, `Volume`.

Les données sont sauvegardées localement sous forme de fichier CSV (`data/cac40_latest.csv`) pour un usage flexible et reproductible.

---

## 🧠 Choix du modèle

Un **modèle LSTM (Long Short-Term Memory)** a été utilisé pour ses performances reconnues dans la modélisation de séries temporelles financières. Détails du modèle :

- Architecture :  
  - 2 couches LSTM avec `Dropout`,
  - 1 couche Dense finale pour la prédiction,
- Fenêtre temporelle (window size) de **60 jours** pour prédire le jour suivant,
- Normalisation des données avec `MinMaxScaler`,
- Entraînement sur **TensorFlow / Keras**.

Le modèle est ensuite sauvegardé dans le dossier `model/` (`cac40_lstm.h5`) pour réutilisation lors de la prédiction.

---

## 🖥️ Fonctionnement de l’application

Le projet est découpé en **4 scripts principaux** :

### 1. `data_preprocessing.py`

- Télécharge les données CAC 40 avec `yfinance`,
- Nettoie, structure et transforme les données pour le LSTM.

### 2. `model.py`

- Définit l’architecture du modèle LSTM,
- Utilise `Sequential` de `tensorflow.keras.models`.

### 3. `train_model.py`

- Charge les données prétraitées,
- Entraîne le modèle LSTM,
- Sauvegarde le modèle dans le dossier `model/`.

### 4. `predict.py`

- Charge le modèle et les dernières données,
- Effectue la prédiction de la **prochaine valeur de clôture**,
- Affiche le résultat dans la console ou l’interface.

---

## 🌐 Interface Streamlit

L’application Streamlit permet :

- De visualiser le **graphique historique** de l’indice CAC 40,
- De lancer la **prédiction pour la journée suivante**,
- De comparer la dernière vraie valeur avec la prédiction du modèle,
- D’intégrer **TradingView** (en option) pour une vue en temps réel du marché.

### Vidéo de démonstration 📹

👉 [Clique ici pour voir la démo de la WebApp sur Google Drive](https://drive.google.com/drive/folders/1mEXAjKg-vCgXeArxqmXDLxjJt7pAo05m?usp=drive_link)

---

## ✅ Fonctionnalités

✔️ Téléchargement automatisé des données CAC 40  
✔️ Modèle LSTM optimisé pour séries temporelles  
✔️ Prédiction de la prochaine valeur de clôture  
✔️ Visualisation interactive avec Streamlit  
✔️ Pipeline complet de bout en bout  
✔️ Intégration facultative de TradingView  

---

## 📁 Structure du projet

Projet-CAC40/
│
├── web_app/                      # (Optionnel) Interface utilisateur avec Streamlit
│   └── app.py                    # Script principal de l'application web
│
├── src/                          # Scripts sources
│   ├── data_preprocessing.py     # Téléchargement et transformation des données CAC 40
│   ├── model.py                  # Définition et compilation du modèle LSTM
│   └── predict.py                # Script de prédiction (utilise le modèle et les données prétraitées)
│
├── train_model.py                # Entraînement du modèle LSTM à partir des données
│
├── data/                         # Données brutes ou traitées
│   └── cac40_latest.csv          # Données historiques du CAC 40 téléchargées via yfinance
│
├── model/                        # Modèle sauvegardé après entraînement
│   └── cac40_lstm.h5             # Fichier du modèle LSTM entraîné (format Keras HDF5)
│
├── requirements.txt              # Liste des dépendances Python (yfinance, pandas, sklearn, tensorflow, etc.)
│
└── README.md                     # Documentation du projet


yaml
Copier
Modifier

---

## ⚙️ Lancer le projet

```bash
git clone https://github.com/ton-utilisateur/cac40-lstm.git
cd cac40-lstm
python -m venv env
env\Scripts\activate        # Ou source env/bin/activate sur Mac/Linux
pip install -r requirements.txt
python train_model.py       # Entraînement
streamlit run web_app/app.py
🔧 Contenu de requirements.txt
txt
Copier
Modifier
pandas
numpy
yfinance
scikit-learn
tensorflow
streamlit
🚫 Limitations connues
La prédiction repose uniquement sur la variable Close, sans indicateurs techniques (MACD, RSI, etc.) pour l’instant.

Le modèle LSTM, bien que performant, peut subir un surapprentissage si les données ne sont pas bien préparées.

Les données de Yahoo Finance peuvent occasionnellement échouer si l’API est instable.

👨‍💻 Auteur
Ce projet a été entièrement réalisé en autonomie par :

Diallo Mamadou Cherif
📬 [Ajouter votre email ou profil LinkedIn/GitHub ici]
