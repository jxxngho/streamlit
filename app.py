import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Map")
df = pd.DataFrame(np.random.randn(500,2)/[50,50]+[30,30]+[37.76,-122.4],columns=['lat','lon'])
st.map(df)

x = st.slider('Selcet a value')
st.write(x, 'squared is', x*x)

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins = 15)
st.pyplot(fig)

st.number_input('Pick a number' ,0 ,10)


st.graphviz_chart('''
  digraph {
    Big_shark -> Tuna
    Tuna -> Mackerel
    Mackerel -> Small_fishes
    Small_fishes -> Shrimp
    }
''')
    
