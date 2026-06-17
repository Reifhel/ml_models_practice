import streamlit as st
import pandas as pd

# Load the data and save on streamlit cache


@st.cache_data
def load_data():
    return pd.read_csv('./output/notebook_clusterization.csv')


df = load_data()

# Sidebar with filter
st.sidebar.header("Filters")

model = st.sidebar.selectbox('Select model', df['model'].unique())

# Filter model
df_notebook_model = df[df['model'] == model]

# Filtering choosen model cluster
df_final_notebook = df[df['cluster'] == df_notebook_model.iloc[0]['cluster']]

st.write("Model Recomendations")
st.table(df_final_notebook)
