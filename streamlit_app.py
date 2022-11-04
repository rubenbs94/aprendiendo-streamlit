# Core Packages
import streamlit as st
import altair as alt

# Exploratory data analysis Packages
import pandas as pd
import numpy as np
from datetime import datetime

# Utils
import joblib

pipeline = joblib.load(
    open("model/model.pkl", "rb")
)
# Function to connect with our ML model
    



# Main Application
def main():
    st.title("Movie Review classifier App")
    with st.form(key="emotion_clf_form"):
        raw_text = st.text_area("Type Here")
        submit_text = st.form_submit_button(label="Submit")

    if submit_text:
        col1, col2 = st.columns(2)

        # Apply the linkage function here
        results = pipeline.predict(raw_text)
        st.write("{}".format(results))
   







if __name__ == "__main__":
    main()
