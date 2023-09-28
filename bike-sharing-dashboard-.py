# ===============================================================
#           CREATE DASHBOARD BIKE SHARING USING STREAMLIT       =
#           ---------------------------------------------       =
# Nama          : Maulana Kavaldo                               =
# Email         : alkav.maulana@gmail.com                       =
# Id Dicoding   : dicoding.com/users/maulanakavaldo/            =
# Github Pages  : maulanakavaldo.github.io                      =
# Created       : 28 September 2023                             =
# ===============================================================

# Import Library
import streamlit as st
import pandas as pd
# import plotly.express as px

# ==============================
# LOAD DATA
# ==============================


@st.cache_resource
def load_data():
    data = pd.read_csv("Bike-sharing-dataset/hour.csv")
    return data


data = load_data()


# ==============================
# TITLE DASHBOARD
# ==============================
# Set page title
st.title("Bike Share Dashboard")

# ==============================
# SIDEBAR
# ==============================
st.sidebar.title("Information:")
st.sidebar.markdown("**• Nama: Maulana Kavaldo**")
st.sidebar.markdown(
    "**• Email: [alkav.maulana@gmail.com](alkav.maulana@gmail.com)**")
st.sidebar.markdown(
    "**• Dicoding: [maulanakavaldo](https://www.dicoding.com/users/maulanakavaldo/)**")
st.sidebar.markdown(
    "**• LinkedIn: [Maulana Kavaldo](https://www.linkedin.com/in/maulana-kavaldo/)**")
st.sidebar.markdown(
    "**• Github: [maulanakavaldo](https://maulanakavaldo.github.io/)**")


st.sidebar.title("Dataset Bike Share")
# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(data)

# Display summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data.describe())

# Show dataset source
st.sidebar.markdown("[Download Dataset](https://link-to-your-dataset)")

st.sidebar.markdown('**Weather:**')
st.sidebar.markdown('1: Clear, Few clouds, Partly cloudy, Partly cloudy')
st.sidebar.markdown('2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist')
st.sidebar.markdown('3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds')
st.sidebar.markdown('4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog')


# ==============================
# VISUALIZATION
# ==============================

# create a layout with two columns
col1, col2 = st.columns(2)
# Load the data
# data = pd.read_csv('your_data.csv')  # Ganti 'your_data.csv' dengan nama file data Anda

with col1:
# Season-wise bike share count
    st.subheader("Season-wise Bike Share Count")

    # Mapping dari angka ke label musim
    season_mapping = {1: "spring", 2: "summer", 3: "fall", 4: "winter"}
    data["season_label"] = data["season"].map(season_mapping)

    season_count = data.groupby("season_label")["cnt"].sum().reset_index()

    # Visualisasi dengan st.bar_chart
    st.bar_chart(season_count.set_index("season_label"))

with col2:
    # Weather situation-wise bike share count
    st.subheader("Weather Situation-wise Bike Share Count")

    weather_count = data.groupby("weathersit")["cnt"].sum().reset_index()

    # Visualisasi dengan st.bar_chart
    st.bar_chart(weather_count.set_index("weathersit"))

# Hourly bike share count
st.subheader("Hourly Bike Share Count")

hourly_count = data.groupby("hr")["cnt"].sum().reset_index()

# Visualisasi dengan st.line_chart
st.line_chart(hourly_count.set_index("hr"))

# Humidity vs. Bike Share Count
st.subheader("Humidity vs. Bike Share Count")

# Visualisasi dengan st.scatter_chart
st.scatter_chart(data=data, x="hum", y="cnt")

# Wind Speed vs. Bike Share Count
st.subheader("Wind Speed vs. Bike Share Count")

# Visualisasi dengan st.scatter_chart
st.scatter_chart(data=data, x="windspeed", y="cnt")

# Temperature vs. Bike Share Count
st.subheader("Temperature vs. Bike Share Count")

# Visualisasi dengan st.scatter_chart
st.scatter_chart(data=data, x="temp", y="cnt")


# Show data source and description
st.sidebar.title("About")
st.sidebar.info("Dashboard ini menampilkan visualisasi untuk sekumpulan data Bike Share. "
                "Dataset ini mengandung informasi mengenai penyewaan sepeda berdasarkan berbagai variabel seperti musim, suhu, kelembaban, dan faktor lainnya.")
