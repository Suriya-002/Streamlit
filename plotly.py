import streamlit as st

import pandas as pd
import numpy as np
import plotly.express as px


def main():
    st.title("Plotting in streamlit with plotly")
    df = pd.read_csv("C://Users//SURIYA//Documents//StreamLit//streamlit//code//streamlit-practice//stacked.csv")
    st.dataframe(df)

    fig = px.pie(df, values="Sum", names="lang", title="Pie chart of languages")
    st.plot(fig)



if __name__ == "__main_":
    main()
