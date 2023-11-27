# Streamlit Documentation: https://docs.streamlit.io/


import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image  # to deal with images (PIL: Python imaging library)

# title of the sidebar
html_temp = """
<div style="background-color:green;padding:10px">
<h2 style="color:white;text-align:center;">Car Price Prediction </h2>
</div>"""
st.sidebar.markdown(html_temp,unsafe_allow_html=True)

# title of the body
html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit ML Cloud App</h2>
</div>"""
st.markdown(html_temp, unsafe_allow_html=True)


# defining variables for user input "km", "Gears", "Displacement_cc","Weight_kg", "Type"
hp_kW = st.sidebar.slider("What is the Hourse power in kW?", 40, 294, step=1)
age = st.sidebar.slider("What is the age of the car?", 0, 3, step=1)
km = st.sidebar.slider("What is total KM the has car?", 0, 317000, step=100)
make_model = st.sidebar.selectbox("What is car's Model?",("Opel Corsa","Renault Clio","Opel Astra","Opel Insignia","Audi A1","Audi A3","Renault Espace"))
Fuel = st.sidebar.selectbox("What is car's Fuel Type", ("Diesel","Benzine","LPG/CNG","Electric"))
Type = st.sidebar.selectbox("What is car's Use status?", ("Used", "New", "Pre-registered", "Employee's car", "Demonstration"))



# converting user inputs into dictionary format
my_dict = {
    "hp_kW": hp_kW,
    "age": age,
    "km": km,
    'make_model': make_model,
    "Fuel": Fuel,
    "Type": Type
}

# To load machine learning model
import pickle
filename = "final_model"
model=pickle.load(open(filename, "rb"))


df = pd.DataFrame.from_dict([my_dict])
st.table(df)

# Prediction with user inputs
predict = st.button("Predict")
result = model.predict(df)
if predict :
    st.success(result[0])
