import streamlit as st

import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()
df = pd.read_csv(iris)

st.dataframe(df)
st.table(df)



st.dataframe(df.style.highlight_max(axis=0))


st.write(df.head())


mycode = """
def hello():
   print("Hello World")
end
"""
