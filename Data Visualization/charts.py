import streamlit as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    st.title("Charts with Streamlit")
    df = pd.read_csv("C:\\Users\\SURIYA\\Documents\\StreamLit\\Python Streamlit\\iris.csv")

    st.dataframe(df.head())

    #Bar Chart using St.bar_chart

    st.bar_chart(df[['sepal_length', "petal_length"]])





if __name__ == "__main__":
    main()
