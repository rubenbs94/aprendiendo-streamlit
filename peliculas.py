import streamlit as st
import pandas as pd
import plotly.express as px

# Carga de datos
data = pd.read_csv('peliculas.csv')

# Extraer categorías únicas de géneros
unique_genres = set()
data['Genre'].apply(lambda x: unique_genres.update(x.split(',')))
unique_genres = sorted(list(unique_genres))

# Sidebar para filtros
st.sidebar.header('Filtros')
selected_genre = st.sidebar.selectbox('Género', options=['All'] + unique_genres)
selected_director = st.sidebar.selectbox('Director', options=['All'] + list(data['Director'].unique()))
selected_actor = st.sidebar.text_input('Actor')

# Filtrado de datos
if selected_genre != 'All':
    data = data[data['Genre'].str.contains(selected_genre)]
if selected_director != 'All':
    data = data[data['Director'] == selected_director]
if selected_actor:
    data = data[data['Actors'].str.contains(selected_actor, case=False, na=False)]

# Mostrar datos filtrados
st.write(data[['Title', 'Genre', 'Director', 'Actors', 'Year', 'Revenue (Millions)', 'Rating']])

# Gráfico de ingresos vs puntuación
if not data.empty:
    fig = px.scatter(data, x='Revenue (Millions)', y='Rating', hover_data=['Title'], title='Ingresos vs Puntuación de Películas')
    st.plotly_chart(fig)

# Correr esto en la terminal:
# streamlit run your_script_name.py
