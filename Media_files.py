import streamlit as st

from PIL import Image

img = Image.open("C:/Users/SURIYA/Downloads/yannick-pulver-hopX_jpVtRM-unsplash.jpg")

st.image(img, use_column_width=True)

