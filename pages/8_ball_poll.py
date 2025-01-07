import streamlit as st
import pandas as pd

st.set_page_config(
  page_icon=":material/sports_and_outdoors:",
  page_title="8 Ball Pool",
  layout="wide"
)

df_data = st.session_state["data"]

ball_pool = df_data[df_data["App Name"] == "8 Ball Pool"]

st.dataframe(ball_pool, width=1500, height=500, column_config={
  "App": st.column_config.ImageColumn()
  })

col1, col2, col3 = st.columns(3)