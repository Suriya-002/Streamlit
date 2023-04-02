import streamlit as st

#import streamlit.components.v1 as components


import streamlit.components.v1 as stc


def main():
    st.title("Streamlit Static Components")

    stc.html("<p style='color:red'>Streamlit is Awsome</p>")
    st.markdown("<p style='color:blue'>Streamlit is Awsome</p>", unsafe_allow_html=True)


    stc.iframe("https://jcharistech.com", scrolling=True)



if __name__ == "__main__":
    main()
