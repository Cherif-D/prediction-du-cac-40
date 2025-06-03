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

---

## ✅ Fonctionnalités

✔️ Téléchargement automatisé des données CAC 40  
✔️ Modèle LSTM optimisé pour séries temporelles  
✔️ Prédiction de la prochaine valeur de clôture  
✔️ Visualisation interactive avec Streamlit  
✔️ Pipeline complet de bout en bout  
✔️ Intégration facultative de TradingView 


---

##👨‍💻 Auteur
Ce projet a été réalisé en autonomie par :

Mamadou Cherif DIALLO
Dans le cadre de mon mémoire de master 1 qui portait sur le machine learning et les marchés financiers.
