import streamlit as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def main():
    st.title("Plotting with plotly")
    df = pd.read_csv("C:\\Users\\SURIYA\\Documents\\StreamLit\\Python Streamlit\\iris.csv")

    st.dataframe(df.head())

    fig = px.pie(df, values="petal_length", title="Pie Chart")
    st.plotly_chart(fig)





if __name__ == "__main__":
    main()
