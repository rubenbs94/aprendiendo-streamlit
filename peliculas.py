import streamlit as st
import pandas as pd

# Carga de datos
data = pd.read_csv('peliculas.csv')

# Sidebar para filtros
st.sidebar.header('Filtros')
selected_genre = st.sidebar.selectbox('Género', options=['All'] + list(data['Genre'].unique()))
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

# Correr esto en la terminal:
# streamlit run your_script_name.py
