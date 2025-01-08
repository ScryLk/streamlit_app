import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_icon=":material/sports_and_outdoors:",
    page_title="8 Ball Pool",
    layout="wide"
)


if "data" not in st.session_state:
    st.error("Erro: Os dados ainda não foram carregados. Volte para a página inicial primeiro.")
    st.stop()


df_data = st.session_state["data"]
social_usage = st.session_state["Social Usage"]
social_opened = st.session_state["Social Opened"]
social_notifications = st.session_state["Social Notifications"]

facebook = df_data[df_data["App Name"] == "Facebook"]

st.dataframe(facebook, width=1500, height=500, column_config={
    "App": st.column_config.ImageColumn()
})


col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📊 Uso Total (min)")
    facebook_usage_sum = facebook["Usage (minutes)"].sum()
    st.metric(label="Total", value=f"{facebook_usage_sum} min")

with col2:
    st.subheader("🔄 Número de Aberturas")
    facebook_opened_sum = facebook["Times Opened"].sum()
    st.metric(label="Total", value=f"{facebook_opened_sum}")

with col3:
    st.subheader("🔔 Total de Notificações")
    facebook_notifications_sum = facebook["Notifications"].sum()
    st.metric(label="Total", value=f"{facebook_notifications_sum}")


st.write("### 📲 Uso do aplicativo por usuário")
facebook_usage = facebook.groupby("ID")["Usage (minutes)"].sum().reset_index()


st.bar_chart(facebook_usage, x="ID", y="Usage (minutes)")
