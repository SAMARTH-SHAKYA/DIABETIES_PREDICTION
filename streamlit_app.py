import streamlit as st
import pandas as pd


st.title('Diabeties prediction app')

st.info('Help to predict diabeties')
data = pd.read_csv('https://github.com/SAMARTH-SHAKYA/DIABETIES_PREDICTION/blob/master/diabetes.csv')
data
