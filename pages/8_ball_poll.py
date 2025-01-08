import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_icon=":material/sports_and_outdoors:",
    page_title="8 Ball Pool",
    layout="wide"
)

# Verificar se os dados foram carregados corretamente no session_state
if "data" not in st.session_state:
    st.error("Erro: Os dados ainda não foram carregados. Volte para a página inicial primeiro.")
    st.stop()

# Carregar dados do session_state
df_data = st.session_state["data"]
social_usage = st.session_state["Social Usage"]
social_opened = st.session_state["Social Opened"]
social_notifications = st.session_state["Social Notifications"]

# Filtrar apenas os dados do 8 Ball Pool
ball_pool = df_data[df_data["App Name"] == "8 Ball Pool"]

# Exibir DataFrame filtrado na interface
st.dataframe(ball_pool, width=1500, height=500, column_config={
    "App": st.column_config.ImageColumn()
})

# Criando layout de 3 colunas
col1, col2, col3 = st.columns(3)

# Criando gráficos e métricas relevantes
with col1:
    st.subheader("📊 Uso Total (min)")
    ball_pool_usage_sum = ball_pool["Usage (minutes)"].sum()
    st.metric(label="Total", value=f"{ball_pool_usage_sum} min")

with col2:
    st.subheader("🔄 Número de Aberturas")
    ball_pool_opened_sum = ball_pool["Times Opened"].sum()
    st.metric(label="Total", value=f"{ball_pool_opened_sum}")

with col3:
    st.subheader("🔔 Total de Notificações")
    ball_pool_notifications_sum = ball_pool["Notifications"].sum()
    st.metric(label="Total", value=f"{ball_pool_notifications_sum}")

# Gráfico de uso por usuário
st.write("### 🎱 Uso do aplicativo por usuário")
ball_pool_usage = ball_pool.groupby("ID")["Usage (minutes)"].sum().reset_index()

# Exibir gráfico de barras com Streamlit
st.bar_chart(ball_pool_usage, x="ID", y="Usage (minutes)")
