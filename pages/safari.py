import streamlit as st
import pandas as pd

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

safari = df_data[df_data["App Name"] == "Safari"]

st.dataframe(safari, width=1500, height=500, column_config={
    "App": st.column_config.ImageColumn()
})


col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📊 Uso Total (min)")
    safari_usage_sum = safari["Usage (minutes)"].sum()
    st.metric(label="Total", value=f"{safari_usage_sum} min")

with col2:
    st.subheader("🔄 Número de Aberturas")
    safari_opened_sum = safari["Times Opened"].sum()
    st.metric(label="Total", value=f"{safari_opened_sum}")

with col3:
    st.subheader("🔔 Total de Notificações")
    safari_notifications_sum = safari["Notifications"].sum()
    st.metric(label="Total", value=f"{safari_notifications_sum}")


st.write("### 🎬 Uso do aplicativo por usuário")
safari_usage = safari.groupby("ID")["Usage (minutes)"].sum().reset_index()


st.bar_chart(safari_usage, x="ID", y="Usage (minutes)")
