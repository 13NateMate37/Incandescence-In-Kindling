import streamlit as st
from character import Character

# The title of the project
st.title("Incandescence In Kindling")
st.write("Create your character to begin your adventure!")

# Storing user input for chaacter name
name = st.text_input("Enter your character's name:")

# Creating a selection for the character's background
background = st.selectbox(
    "Choose your character's background:",
    ["Acolyte", "Foreigner", "Noble", "Outlander", "Sage", "Warrior"]
)

# Creating a character with the user input
if st.button("Create Character"):
    st.session_state.character = Character(
        name=name,
        background=background
    )    

    # Fancier output for the user
    st.success("Character successfully created!")

if "character" in st.session_state:
    character = st.session_state.character

    st.subheader("Your Character Details")

    st.write(f"Name: {character.name}")
    st.write(f"Background: {character.background}")
    st.write(f"Level: {character.level}")
    st.write(f"EXP: {character.xp}")
    st.write(f"HP: {character.hp}")
    st.write(f"Inventory: {character.inventory}")


