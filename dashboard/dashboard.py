import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Bike Sharing Dashboard")

# Load dataset
data = pd.read_csv("dashboard/main_data.csv")

# mapping musim
season_map = {
    1: "1. Musim Semi",
    2: "2. Musim Panas",
    3: "3. Musim Gugur",
    4: "4. Musim Dingin"
}

data["season_name"] = data["season"].map(season_map)

# SIDEBAR FILTER

st.sidebar.header("Filter Data")

season_filter = st.sidebar.multiselect(
    "Pilih Musim",
    data["season_name"].unique(),
    default=data["season_name"].unique()
)

year_filter = st.sidebar.multiselect(
    "Pilih Tahun",
    data["yr"].unique(),
    default=data["yr"].unique()
)

weather_filter = st.sidebar.multiselect(
    "Pilih Cuaca",
    data["weathersit"].unique(),
    default=data["weathersit"].unique()
)

# FILTER DATASET

filtered_data = data[
    (data["season_name"].isin(season_filter)) &
    (data["yr"].isin(year_filter)) &
    (data["weathersit"].isin(weather_filter))
]

# SUMMARY METRICS

st.subheader("Ringkasan Penyewaan Sepeda")

col1, col2, col3 = st.columns(3)

col1.metric("Total Penyewaan", int(filtered_data["cnt"].sum()))
col2.metric("Rata-rata Penyewaan", int(filtered_data["cnt"].mean()))
col3.metric("Penyewaan Tertinggi", int(filtered_data["cnt"].max()))

# DATA PREVIEW

st.subheader("Dataset Preview")
st.write(filtered_data.head())

# GRAFIK 1

st.subheader("Rata-rata Penyewaan Sepeda per Bulan")

fig, ax = plt.subplots()
sns.barplot(x="mnth", y="cnt", data=filtered_data, ax=ax)

ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Penyewaan")

st.pyplot(fig)

# GRAFIK 2

st.subheader("Penyewaan Sepeda Berdasarkan Musim")

fig2, ax2 = plt.subplots()
sns.barplot(x="season_name", y="cnt", data=filtered_data, ax=ax2)

ax2.set_xlabel("Musim")
ax2.set_ylabel("Jumlah Penyewaan")

st.pyplot(fig2)