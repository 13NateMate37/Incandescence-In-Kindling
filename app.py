import streamlit as st
from character import Character


st.title("TGA Precursor")

# Storing user input for chaacter name
name = st.text_input("Enter your character's name:")
st.write("Your name is: ", name)

# Creating a selection for the character's background
background = st.selectbox(
    "Choose your character's background:",
    ["Acolyte", "Foreigner", "Noble", "Outlander", "Sage", "Warrior"]
)


