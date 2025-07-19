import streamlit as st

st.title("About Page")
st.header("ℹ️ Welcome to the About Page!")

with open("README.md", "r") as file:
    text = "\n".join([
        line.strip() for line in file.readlines()
    ])

st.markdown(text)