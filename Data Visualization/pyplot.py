import streamlit as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import seaborn as sns

def main():
    st.title("Plotting with Pyplot")
    df = pd.read_csv("C:\\Users\\SURIYA\\Documents\\StreamLit\\Python Streamlit\\iris.csv")

    st.dataframe(df.head())


    #Previous Method
    # df['species'].value_counts().plot(kind="bar")
    # st.pyplot()

    # plt.scatter(*np.random.random(size=(2,100)))
    # st.pyplot()

    # Recommended Method

    fig = plt.figure(figsize=(12,10))
    df['species'].value_counts().plot(kind="bar")
    st.pyplot(fig)




if __name__ == "__main__":
    main()
