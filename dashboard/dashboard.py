import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Bike Sharing Dashboard")

data = pd.read_csv("../data/day.csv")

st.write("Dataset Preview")
st.write(data.head())

fig, ax = plt.subplots()
sns.barplot(x="season", y="cnt", data=data, ax=ax)

st.pyplot(fig)