import streamlit as st

st.text("Hello World this is a text")

name = "Suriya"

st.text("This is so {}".format(name))

st.header("This is a header")

st.subheader("This is a subheader")

st.title("This is a title")

st.markdown("## This is a markdown")


st.success("Successful")
st.warning("This is Danger")
st.info("This is information")
st.error("This is error")



st.write("## this is a text")
st.write(1+2)
