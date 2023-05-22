import altair as alt
import pandas as pd
import streamlit as st
import pickle
import numpy as np

# Загрузка моделей
with open('new_model.pkl', 'rb') as alc_model_pkl:
    lr_alc = pd.read_pickle(alc_model_pkl)
with open('drug_model.pkl', 'rb') as drug_model_pkl:
    lr_drug = pd.read_pickle(drug_model_pkl)

col1, col2= st.columns(2)

# Данные введенные пользователем
unseen = st.slider("Количество безработных (в тыс. человек)", min_value = 20.0, max_value = 200.0, step = 0.1)
decimal = st.slider("Знаки после запятой", min_value = 0, max_value = 10, step = 1)
X_test_sm = [[float(1.0)], [float(unseen)]]
X_test_sm = np.squeeze(X_test_sm)

# Прогноз
result_alc = lr_alc.predict(X_test_sm)[0]
result_drug = lr_drug.predict(X_test_sm)[0]

@st.cache_data
def flags():
    a = result_alc
    b = result_drug
    return a, b

delta_alc, delta_drug = flags()

st.write("Нажмите на кнопку, затем укажите сверху данные (количество безработных), которые хотите сравнивать.")
if st.button("Сравнить"):
    st.cache_data.clear()
    
# Вывод
if (result_alc > 0) and (result_drug > 0):
    col1.metric(label = "Количество алкоголиков", value = str(result_alc)[:(len(str(int(result_alc))) + decimal + 1)], delta = str(result_alc-delta_alc)[:(len(str(int(result_alc-delta_alc))) + decimal + 1)], delta_color = "inverse")
    col2.metric(label = "Количество наркоманов", value = str(result_drug)[:(len(str(int(result_drug))) + decimal + 1)], delta = str(result_drug-delta_drug)[:(len(str(int(result_drug-delta_drug))) + decimal + 1)], delta_color = "inverse")
    source1 = pd.DataFrame({
    'Прогноз': ['Безраб.', 'Алк.', 'Нарк.'],
    'Количество людей в тыс': [unseen, result_alc, result_drug]})
    source2 = pd.DataFrame({
    'Прогноз': ['Алк.', 'Нарк.'],
    'Количество людей в тыс': [result_alc, result_drug]})
else:
    col1.metric(label = "Количество алкоголиков", value = 0, delta = str(result_alc-delta_alc)[:(len(str(int(result_alc-delta_alc))) + decimal + 1)], delta_color = "inverse")
    col2.metric(label = "Количество наркоманов", value = 0, delta = str(result_drug-delta_drug)[:(len(str(int(result_drug-delta_drug))) + decimal + 1)], delta_color = "inverse")
    source1 = pd.DataFrame({
    'Прогноз': ['Безраб.', 'Алк.', 'Нарк.'],
    'Количество людей в тыс': [unseen, 0, 0]})
    source2 = pd.DataFrame({
    'Прогноз': ['Алк.', 'Нарк.'],
    'Количество людей в тыс': [0, 0]})
      
tab1, tab2 = st.tabs(["График А/Н", "График А/Б/Н"])
with tab1:
    st.altair_chart(alt.Chart(pd.DataFrame(source2)).mark_bar().encode(x = 'Прогноз', y = 'Количество людей в тыс'), use_container_width = True)
with tab2:
    st.altair_chart(alt.Chart(pd.DataFrame(source1)).mark_bar().encode(x = 'Прогноз', y = 'Количество людей в тыс'), use_container_width = True)





