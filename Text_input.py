import streamlit as st

fname = st.text_input("Enter your name")
#text input
st.title(fname)

#Text input hide password

password = st.text_input("Enter your password", type="password")

#text area
message = st.text_area("Enter Message")
st.write(message)

#numbers

number = st.number_input("Enter Number")

#Date Input

myappointment = st.date_input("Appointment")

#Time Input

mytime = st.time_input("MY Time")


#Color picker

color = st.color_picker("Select Color")
