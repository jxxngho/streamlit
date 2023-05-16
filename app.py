import streamlit as st

x = st.slider('Selcet a value')
st.write(x, 'squared is', x*x)
