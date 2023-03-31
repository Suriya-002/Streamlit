import streamlit as st

my_lang = ["Python", "Ruby", "Rust", "Go"]

choice = st.selectbox("Prefer your language", my_lang)
st.write("You have selected {} as you language".format(choice))


#Multiple selection

spoken_lang = ("English", "French", "Japanese", "German", "Spanish")

my_lang = st.multiselect("Spoken language", spoken_lang, default="English")


#Slider

age = st.slider("Age", 1,100,5)
