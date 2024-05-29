import streamlit as st
import pandas as pd

# Carga de datos
data = pd.read_csv('path_to_your_file.csv')

# Sidebar para filtros
st.sidebar.header('Filtros')
selected_genre = st.sidebar.multiselect('Género', options=data['Genre'].unique(), default=data['Genre'].unique())
selected_director = st.sidebar.multiselect('Director', options=data['Director'].unique(), default=data['Director'].unique())
selected_actor = st.sidebar.text_input('Actor')

# Filtrado de datos
filtered_data = data[data['Genre'].isin(selected_genre) & data['Director'].isin(selected_director)]
if selected_actor:
    filtered_data = filtered_data[filtered_data['Actors'].str.contains(selected_actor, case=False, na=False)]

# Mostrar datos filtrados
st.write(filtered_data[['Title', 'Genre', 'Director', 'Actors', 'Year', 'Revenue (Millions)', 'Rating']])

# Correr esto en la terminal:
# streamlit run your_script_name.py
