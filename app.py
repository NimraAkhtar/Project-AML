#import joblib
#joblib.dump(model,'lr_model.pkl')
import pandas as pd

import joblib

import streamlit as st

#Load the Model

model= joblib.load('./model.pkl')

#UI Elements, to get input

st.title('Car Price Prediction')

make = st.number_input('make', step=1)
year=st.text_input('year')
mileage = st.number_input('mileage', step=1)
type1 = st.number_input('type1', step=1)
transmission = st.number_input('transmission', step=1)
cc = st.number_input('cc', step=1)

#Format the input data to a dataframe

new_data = pd.DataFrame({'make': make, 'year': year, 'mileage':mileage,'type1': type1, 'transmission':transmission,'cc': cc }, index=[0])

result=""

if st.button("Predict"):
    result = model.predict(new_data)

    st.subheader("Prediction Car price")

    st.subheader(result)

else:
    st.subheader("Enter car data and click Predict button")
