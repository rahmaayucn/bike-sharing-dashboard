import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Bike Sharing Dashboard")

# Baca dataset
data = pd.read_csv("dashboard/main_data.csv")

# FILTER INTERAKTIF
season_filter = st.sidebar.selectbox(
    "Pilih Musim",
    sorted(data["season"].unique())
)

filtered_data = data[data["season"] == season_filter]

st.subheader("Dataset Preview")
st.write(filtered_data.head())

st.subheader("Rata-rata Penyewaan Sepeda per Bulan")

fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x="mnth", y="cnt", data=filtered_data, ax=ax)

ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Penyewaan")

st.pyplot(fig)