import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

st.title("Bike Sharing Dashboard")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "main_data.csv")

data = pd.read_csv(data_path)

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