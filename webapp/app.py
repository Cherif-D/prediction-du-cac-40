import sys
import os
import streamlit as st
import datetime
import plotly.graph_objs as go
from zoneinfo import ZoneInfo
import pandas as pd
import yfinance as yf

# Ajout du dossier src au path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.predict import predict_next_close
from src.data_preprocessing import load_data

# Configuration de la page
st.set_page_config(page_title="Prédiction CAC 40", layout="wide")

# Sidebar - Sélection d'affichage
st.sidebar.header("Paramètres")
analysis_choice = st.sidebar.selectbox("Choisir l'affichage", ["Prédiction du cours", "RSI", "Graphique TradingView"])

# Chargement des données
df = load_data('../data/cac40_latest.csv')


# RSI computation
def compute_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

df['RSI'] = compute_rsi(df)

# Titre
st.title("📈 Application Financière - CAC 40")

# === Bloc : Prédiction ===
if analysis_choice == "Prédiction du cours":
    st.subheader("📅 Prédiction du cours de clôture")

    if st.button("Lancer la prédiction"):
        today = datetime.datetime.today().weekday()
        if today in [5, 6]:
            st.warning("⚠️ Marché fermé le week-end. Affichage de la prédiction du dernier jour ouvré.")
        last_date, prediction = predict_next_close()
        st.write(f"Date de la dernière donnée connue : **{last_date.date()}**")
        st.metric("📊 Cours prédit du CAC 40", f"{prediction:.2f} €")

    # Affichage statistiques
    st.subheader("📊 Statistiques")
    col1, col2, col3 = st.columns(3)
    col1.metric("Prix minimum", f"{df['Close'].min():.2f} €")
    col2.metric("Prix maximum", f"{df['Close'].max():.2f} €")
    col3.metric("Prix moyen", f"{df['Close'].mean():.2f} €")

    # Graphique du cours
    st.subheader("📉 Historique du cours")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close'))
    fig.update_layout(xaxis_title="Date", yaxis_title="Cours (€)", template="plotly_white", height=400)
    st.plotly_chart(fig, use_container_width=True)

# === Bloc : RSI ===
elif analysis_choice == "RSI":
    st.subheader("📊 Indicateur RSI (Relative Strength Index)")
    latest_rsi = df['RSI'].iloc[-1]

    if latest_rsi > 70:
        sentiment = "🔴 Surachat (vente possible)"
    elif latest_rsi < 30:
        sentiment = "🟢 Survente (achat possible)"
    else:
        sentiment = "🟡 Neutre"

    st.write(f"**RSI actuel** : {latest_rsi:.2f}")
    st.success(f"**Sentiment du marché** : {sentiment}")

    # RSI Graph
    fig_rsi = go.Figure()
    fig_rsi.add_trace(go.Scatter(x=df.index, y=df['RSI'], mode='lines', name='RSI', line=dict(color='purple')))
    fig_rsi.add_hline(y=70, line_dash="dash", line_color="red")
    fig_rsi.add_hline(y=30, line_dash="dash", line_color="green")
    fig_rsi.update_layout(title="RSI - CAC 40", height=400, template="plotly_white", xaxis_title="Date", yaxis_title="RSI")
    st.plotly_chart(fig_rsi, use_container_width=True)

# === Bloc : Graphique TradingView ===
elif analysis_choice == "Graphique TradingView":
    st.subheader("📺 Graphique TradingView - CAC 40 (CFD)")

    st.write("""
    ⚠️ **Note** : Le graphique utilise le CFD de l’indice CAC 40 (via OANDA).  
    Les données peuvent légèrement différer de celles de Yahoo Finance.

    👉 Idéal pour **une analyse technique en direct**.
    """)

    # Widget TradingView
    tradingview_widget = """
    <div class="tradingview-widget-container">
      <div id="tradingview_widget"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget(
      {
      "width": "100%",
      "height": 620,
      "symbol": "OANDA:FR40EUR",
      "interval": "D",
      "timezone": "Etc/UTC",
      "theme": "light",
      "style": "1",
      "locale": "fr",
      "toolbar_bg": "#f1f3f6",
      "enable_publishing": false,
      "hide_side_toolbar": false,
      "allow_symbol_change": true,
      "container_id": "tradingview_widget"
      });
      </script>
    </div>
    """
    st.components.v1.html(tradingview_widget, height=640)

