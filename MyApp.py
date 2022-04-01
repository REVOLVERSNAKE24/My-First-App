import streamlit as st
import pandas as pd
st.title("My First App")
#st.button ("Inicio")  
#st.button ("Seccion 1")

df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')

st.write(df)

st.map(df)