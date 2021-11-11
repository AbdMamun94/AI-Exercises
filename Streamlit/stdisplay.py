import streamlit as st

# load EDA pakgs

import pandas as pd

# Display data

df = pd.read_csv("iris.csv")

#mathod1

st.dataframe(df)

#mathod2 : Static Table 

st.table(df)

st.text(" i am here ")