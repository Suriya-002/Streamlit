import streamlit as st



name = "Suriya"

if st.button("Submit"):
    st.write("Name : {}".format(name.upper()))


if st.button("Submit", key="new02"):
    st.write("First Name : {}".format(name.lower()))


#Radio Buttons

status = st.radio("What is your status", ("Active", "Inactive"))

if status=="Active":
    st.success("You are Active")
elif status=="Inactive":
    st.error("You are inactive")

if st.checkbox("Show/Hide"):
    st.text("Showing Something")


#Working with Beta Expander

if st.expander("Python"):
    st.success("Hello PYthon")
