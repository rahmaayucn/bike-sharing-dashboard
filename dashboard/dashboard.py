import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Bike Sharing Dashboard")

data = pd.read_csv("dashboard/main_data.csv")

# mapping musim
season_map = {
    1: "Spring (Musim Semi) 🌸",
    2: "Summer (Musim Panas) ☀️",
    3: "Fall / Autumn (Musim Gugur) 🍂",
    4: "Winter (Musim Dingin) ❄️"
}

data["season_name"] = data["season"].map(season_map)

# FILTER
season_filter = st.sidebar.selectbox(
    "Pilih Musim",
    data["season_name"].unique()
)

filtered_data = data[data["season_name"] == season_filter]

st.subheader("Dataset Preview")
st.write(filtered_data.head())

st.subheader("Rata-rata Penyewaan Sepeda per Bulan")

fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x="mnth", y="cnt", data=filtered_data, ax=ax)

ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Penyewaan")

st.pyplot(fig)