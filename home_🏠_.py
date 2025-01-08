import pandas as pd
import streamlit as st

# Configuração da Página
st.set_page_config(
    layout="wide",
    page_title="Applications",
    page_icon="📲",
    initial_sidebar_state="auto",
)

# Layout de colunas
col1, col2, col3 = st.columns(3)

# Carregar a base de dados
df = pd.read_csv("screentime_analysis.csv")

# Garantindo que a base esteja no session_state para uso global
if "data" not in st.session_state:
    df_data = pd.read_csv("screentime_analysis.csv", index_col=0)
    st.session_state["data"] = df_data
else:
    df_data = st.session_state["data"]

# Ajustes na base de dados
df_data["App Name"] = df_data["App"]
df_data.index = range(1, len(df_data) + 1)
df_data.index.name = "ID"

# Substituir nomes de aplicativos por URLs das imagens (para exibição)
app_images = {
    "Instagram": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/768px-Instagram_icon.png",
    "X": "https://freepnglogo.com/images/all_img/1691832581twitter-x-icon-png.png",
    "WhatsApp": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/1022px-WhatsApp.svg.png",
    "8 Ball Pool": "https://upload.wikimedia.org/wikipedia/en/0/0c/8_Ball_Pool_cover.jpg",
    "Safari": "https://support.apple.com/content/dam/edam/applecare/images/en_US/psp/psp_heroes/mini-hero-safari.png",
    "Netflix": "https://w7.pngwing.com/pngs/299/104/png-transparent-netflix-logo-logos-brands-in-colors-icon-thumbnail.png",
    "Facebook": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Facebook_logo_%28square%29.png/640px-Facebook_logo_%28square%29.png",
    "LinkedIn": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToJQcThrVQw9sab54dutfCQcfwmQ4D0HbrcQ&s",
}

df_data.replace(app_images, inplace=True)
df_data["App Name"].replace({v: k for k, v in app_images.items()}, inplace=True)

# Exibir a base de dados na interface
st.dataframe(df_data, width=1500, height=500, column_config={
    "App": st.column_config.ImageColumn()
})

# Lista de aplicativos a serem analisados
apps = ["Instagram", "X", "WhatsApp", "8 Ball Pool", "Safari", "Netflix", "Facebook", "LinkedIn"]

# Criar dicionários para armazenar métricas por aplicativo
usage_data = {}
opened_data = {}
notifications_data = {}

# Loop para calcular os dados de cada aplicativo
for app in apps:
    app_data = df_data[df_data["App Name"] == app]
    
    # Tempo de uso total
    usage_data[app] = app_data.groupby("ID")["Usage (minutes)"].sum().sum()
    
    # Número de vezes que o app foi aberto
    opened_data[app] = app_data.groupby("ID")["Times Opened"].sum().sum()
    
    # Número de notificações recebidas
    notifications_data[app] = app_data.groupby("ID")["Notifications"].sum().sum()

# Criar DataFrames organizados para gráficos
social_usage = pd.DataFrame({"App": list(usage_data.keys()), "Usage (minutes)": list(usage_data.values())})
social_opened = pd.DataFrame({"App": list(opened_data.keys()), "Times Opened": list(opened_data.values())})
social_notifications = pd.DataFrame({"App": list(notifications_data.keys()), "Notifications": list(notifications_data.values())})

# Criar gráficos no Streamlit
st.write("### Usage Minutes")
st.bar_chart(data=social_usage, x="App", y="Usage (minutes)")

st.write("### Opened Times")
st.bar_chart(data=social_opened, x="App", y="Times Opened")

st.write("### Notifications")
st.bar_chart(data=social_notifications, x="App", y="Notifications")

# Armazenando DataFrames no `st.session_state` para acesso em outros arquivos
st.session_state["Social Usage"] = social_usage
st.session_state["Social Opened"] = social_opened
st.session_state["Social Notifications"] = social_notifications
