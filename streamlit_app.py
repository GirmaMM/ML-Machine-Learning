import streamlit as st

st.title(' 🤖  Machine Learning App')

st.info('This app bulids a machine learning app')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
