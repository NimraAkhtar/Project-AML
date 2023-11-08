#import joblib
#joblib.dump(model,'lr_model.pkl')
import pandas as pd

import joblib

import streamlit as st

#Load the Model

model= joblib.load('./LogicReg_model.pkl')

#UI Elements, to get input

st.title('Titanic Ship - Person survived or not - prediction')

pclass = st.number_input('pclass', step=1)
sex=st.text_input('sex')
age = st.number_input('age', step=1)
fare = st.number_input('fare', step=1)
family_mem = st.number_input('family_mem', step=1)

#Format the input data to a dataframe

new_data = pd.DataFrame({'pclass': pclass, 'sex': sex, 'age':age,'fare': fare, 'family_mem':family_mem, }, index=[0])

result=""

if st.button("Predict"):
    result = model.predict(new_data)

    st.subheader("Predicted 0 for died and 1 for survived person")

    st.subheader(result)

else:
    st.subheader("Enter person data and click Predict button")