import pandas as pd
import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Aplications",
    page_icon="📲",
    initial_sidebar_state="auto",
)



col1, col2, col3 = st.columns(3)

df = pd.read_csv("screentime_analysis.csv")

if "data" not in st.session_state:
    df_data = pd.read_csv("screentime_analysis.csv", index_col=0)
    st.session_state["data"] = df_data

df_data["App Name"] = df_data["App"]

df_data.index = range(1, 201)
df_data.index.name = "ID"


df_data.replace(
    {
        "Instagram": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/768px-Instagram_icon.png",
        "X": "https://freepnglogo.com/images/all_img/1691832581twitter-x-icon-png.png",
        "WhatsApp": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/1022px-WhatsApp.svg.png",
        "8 Ball Pool": "https://upload.wikimedia.org/wikipedia/en/0/0c/8_Ball_Pool_cover.jpg",
        "Safari": "https://support.apple.com/content/dam/edam/applecare/images/en_US/psp/psp_heroes/mini-hero-safari.png",
        "Netflix": "https://w7.pngwing.com/pngs/299/104/png-transparent-netflix-logo-logos-brands-in-colors-icon-thumbnail.png",
        "Facebook": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Facebook_logo_%28square%29.png/640px-Facebook_logo_%28square%29.png",
        "LinkedIn": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToJQcThrVQw9sab54dutfCQcfwmQ4D0HbrcQ&s",
    },
    inplace=True,
)

df_data["App Name"].replace(
  {
    "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/768px-Instagram_icon.png": "Instagram",
    "https://freepnglogo.com/images/all_img/1691832581twitter-x-icon-png.png": "X",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/1022px-WhatsApp.svg.png": "WhatsApp",
    "https://upload.wikimedia.org/wikipedia/en/0/0c/8_Ball_Pool_cover.jpg": "8 Ball Pool",
    "https://support.apple.com/content/dam/edam/applecare/images/en_US/psp/psp_heroes/mini-hero-safari.png": "Safari",
    "https://w7.pngwing.com/pngs/299/104/png-transparent-netflix-logo-logos-brands-in-colors-icon-thumbnail.png": "Netflix",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Facebook_logo_%28square%29.png/640px-Facebook_logo_%28square%29.png": "Facebook",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToJQcThrVQw9sab54dutfCQcfwmQ4D0HbrcQ&s": "LinkedIn"
  }, inplace=True
)


st.dataframe(df_data, width=1500, height=500, column_config={
  "App": st.column_config.ImageColumn()
  })
#Safari
safari = df_data[df_data["App Name"] == "Safari"]
safari_usage = safari.groupby("ID")["Usage (minutes)"].sum().reset_index()
safari_usage_sum = safari_usage["Usage (minutes)"].sum()
safari_opened = safari.groupby("ID")["Times Opened"].sum().reset_index()
safari_opened_sum = safari_opened["Times Opened"].sum()
safari_notifications = safari.groupby("ID")["Notifications"].sum().reset_index()
safari_notifications_sum = safari_notifications["Notifications"].sum()


#Instagram
instagram = df_data[df_data["App Name"] == "Instagram"]
instagram_usage = instagram.groupby("ID")["Usage (minutes)"].sum().reset_index()
instagram_usage_sum = instagram_usage["Usage (minutes)"].sum()
instagram_opened = instagram.groupby("ID")["Times Opened"].sum().reset_index()
instagram_opened_sum = instagram_opened["Times Opened"].sum()
instagram_notifications = instagram.groupby("ID")["Notifications"].sum().reset_index()
instagram_notifications_sum = instagram_notifications["Notifications"].sum()




#X
x = df_data[df_data["App Name"] == "X"]
x_usage = x.groupby("ID")["Usage (minutes)"].sum().reset_index()
x_usage_sum = x_usage["Usage (minutes)"].sum()
x_opened = x.groupby("ID")["Times Opened"].sum().reset_index()
x_opened_sum = x_opened["Times Opened"].sum()
x_notifications = x.groupby("ID")["Notifications"].sum().reset_index()
x_notifications_sum = x_notifications["Notifications"].sum()




#Whatsapp
whatsapp = df_data[df_data["App Name"] == "WhatsApp"]
whatsapp_usage = whatsapp.groupby("ID")["Usage (minutes)"].sum().reset_index()
whatsapp_usage_sum = whatsapp_usage["Usage (minutes)"].sum()
whatsapp_opened = whatsapp.groupby("ID")["Times Opened"].sum().reset_index()
whatsapp_opened_sum = whatsapp_opened["Times Opened"].sum()
whatsapp_notifications = whatsapp.groupby("ID")["Notifications"].sum().reset_index()
whatsapp_notifications_sum = whatsapp_notifications["Notifications"].sum()





#8 Ball Pool
ball_pool = df_data[df_data["App Name"] == "8 Ball Pool"]
ball_pool_usage = ball_pool.groupby("ID")["Usage (minutes)"].sum().reset_index()
ball_pool_usage_sum = ball_pool_usage["Usage (minutes)"].sum()
ball_pool_opened = ball_pool.groupby("ID")["Times Opened"].sum().reset_index()
ball_pool_opened_sum = ball_pool_opened["Times Opened"].sum()
ball_pool_notifications = ball_pool.groupby("ID")["Notifications"].sum().reset_index()
ball_pool_notifications_sum = ball_pool_notifications["Notifications"].sum()




#Netflix
netflix = df_data[df_data["App Name"] == "Netflix"]
netflix_usage = netflix.groupby("ID")["Usage (minutes)"].sum().reset_index()
netflix_usage_sum = netflix_usage["Usage (minutes)"].sum()
netflix_opened = netflix.groupby("ID")["Times Opened"].sum().reset_index()
netflix_opened_sum = netflix_opened["Times Opened"].sum()
netflix_notifications = netflix.groupby("ID")["Notifications"].sum().reset_index()
netflix_notifications_sum = netflix_notifications["Notifications"].sum()




#Facebook
facebook = df_data[df_data["App Name"] == "Facebook"]
facebook_usage = facebook.groupby("ID")["Usage (minutes)"].sum().reset_index()
facebook_usage_sum = facebook_usage["Usage (minutes)"].sum()
facebook_opened = facebook.groupby("ID")["Times Opened"].sum().reset_index()
facebook_opened_sum = facebook_opened["Times Opened"].sum()
facebook_notifications = facebook.groupby("ID")["Notifications"].sum().reset_index()
facebook_notifications_sum = facebook_notifications["Notifications"].sum()



#Linkedin
linkedin = df_data[df_data["App Name"] == "LinkedIn"]
linkedin_usage = linkedin.groupby("ID")["Usage (minutes)"].sum().reset_index()
linkedin_usage_sum = linkedin_usage["Usage (minutes)"].sum()
linkedin_opened = linkedin.groupby("ID")["Times Opened"].sum().reset_index()
linkedin_opened_sum = linkedin_opened["Times Opened"].sum()
linkedin_notifications = linkedin.groupby("ID")["Notifications"].sum().reset_index()
linkedin_notifications_sum = linkedin_notifications["Notifications"].sum()



social_usage = pd.DataFrame(
    {
        "App": ["Instagram", "X", "WhatsApp", "8 Ball Pool", "Safari", "Netflix", "Facebook", "LinkedIn"],
        "Usage (minutes)": [instagram_usage_sum, x_usage_sum, whatsapp_usage_sum, 
                            ball_pool_usage_sum, safari_usage_sum, netflix_usage_sum, 
                            facebook_usage_sum, linkedin_usage_sum]
    }
)

social_opened = pd.DataFrame(
  {
    "App": ["Instagram", "X", "WhatsApp", "8 Ball Pool", "Safari", "Netflix", "Facebook", "LinkedIn"],
    "Times Opened": [
      instagram_opened_sum, 
      x_opened_sum, 
      whatsapp_opened_sum, 
      ball_pool_opened_sum, 
      safari_opened_sum, 
      netflix_opened_sum, 
      facebook_opened_sum,
      linkedin_opened_sum]
  }
)

social_notifications = pd.DataFrame(
  {
    "App": ["Instagram", "X", "WhatsApp", "8 Ball Pool", "Safari", "Netflix", "Facebook", "LinkedIn"],
    "Notifications": [
      instagram_notifications_sum,
      x_notifications_sum,
      whatsapp_notifications_sum,
      ball_pool_notifications_sum,
      safari_notifications_sum,
      netflix_notifications_sum,
      facebook_notifications_sum,
      linkedin_notifications_sum
    ]
    
  }
)


st.write("Usage Minutes")
st.bar_chart(data=social_usage, x="App", y="Usage (minutes)")
st.write("Opened Times")
st.bar_chart(data=social_opened, x="App", y="Times Opened")
st.write("Notifications")
st.bar_chart(data=social_notifications, x="App", y="Notifications")


st.session_state["Social Usage"] = social_usage
st.session_state["Social Opened"] = social_opened
st.session_state["Social Notifications"] = social_notifications