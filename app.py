import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(page_title='Mi Dashboard')
st.header('📊 Mi dashboard')
movies = pd.read_csv(r'C:\Users\mayrmon\Documents\TripleTen\Sprint_7_Clase_Webinar\sp7_colaborative_project\dataset\imdb_movies.csv')
st.subheader('Películas de IMDB')
st.dataframe(movies)
st.subheader('Gráfico de Películas por Año')
fig = px.histogram(movies, x='Released_Year', title='Número de Películas por Año')
st.plotly_chart(fig, use_container_width=True)
show_df = st.checkbox('Mostrar tabla de películas', value=True)
if show_df:
    st.subheader('Películas de IMDB')
    st.dataframe(movies)
fig, ax = plt.subplots()
movies['Gross']=pd.to_numeric(movies['Gross'].str.replace(',',''),errors='coerce')
movies['Gross'].plot(kind='box', title='Cuartiles de Gross', grid=True)
st.pyplot(fig)
fig = px.box(movies, x='Certificate', y='Gross', title='Boxplot de "Gross" por categoría (Certificate)')
fig.update_layout(
    xaxis_title='Categoría',
    yaxis_title='Valor',
    boxmode='group'  # Por si tienes múltiples trazas en el futuro
)
st.plotly_chart(fig)

