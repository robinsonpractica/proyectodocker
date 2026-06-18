import streamlit as st
import pandas as pd
st.title('our app, DS development')
url = "https://raw.githubusercontent.com/it-ces/Datasets/refs/heads/main/icfes.csv"
df = pd.read_csv(url)
st.dataframe(df.head())
opcion1 = st.selectbox('seleccione genero', df['ESTU_GENERO'].unique())
st.dataframe(df[df['ESTU_GENERO']==opcion1])
st.write('voy a calcular la media de la variable tal sobre el grupo', opcion1)
st.write(df[df['ESTU_GENERO']==opcion1]['PUNT_GLOBAL'].mean())

