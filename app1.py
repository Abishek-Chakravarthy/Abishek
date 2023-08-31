import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
#  App

This app predicts the largest of Three Numbers
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    a = st.number_input("First Number",min_value=2.0,max_value=2000000.0)
    b = st.number_input("Second Number",min_value=2.0,max_value=2000000.0)
    c = st.number_input("Third Number",min_value=2.0,max_value=2000000.0)
    data = {'First Number':a,'Second Number':b,'Third Number':c}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())

st.subheader('Prediction')
if data['First Number']>=data['Second Number'] and data['First Number']>=data['Third Number']:
    st.write('The largest number is',data['First Number'])
elif data['Second Number']>=data['First Number'] and data['Second Number']>=data['Third Number']:
    st.write('The largest number is',data['Second Number'])
else:
    st.write('The largest number is',data['Third Number'])
#st.write(prediction)
