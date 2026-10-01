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

# Creating a character with the user input
if st.button("Create Character"):    
    character = Character(
        name=name,
        background=background
        )

    # Fancier output for the user
    st.success("Character successfully created!")

    # Displaying the character's details
    # Want to neaten that output at some point
    st.write(character)


