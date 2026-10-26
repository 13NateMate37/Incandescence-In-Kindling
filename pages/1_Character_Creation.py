"""
Streamlit character creation page
"""



import streamlit as st

from Stat_Array_Generation import array_Roller_Standard
from Stat_Array_Generation import ABILITY_SCORES_BLANK_BASE





# Checking whether a game has been initialised 
if not st.session_state.get("game_active", False):
    st.warning("Start a game before making character")
    st.stop()


# page title 
st.title("Character Creation")

# Storing the character name
character_name = st.text_input("Enter your character's name.")

# Subheading 
st.subheader("Ability Score Assignment")


# Ability Score generation 
# Loads a standard array into the session state
if st.button("Standard Array"):
    st.session_state.scores = array_Roller_Standard()


# If there's a Stat Array in session state
if "scores" in st.session_state:
    st.write(st.session_state.scores)


# Settin an Ability Score that hasn't been assigned in s
# ession state to none
if "selected_ability" not in st.session_state:
    st.session_state.selected_ability = None

# List to loop through for buttons
ability_score_button_list = [
    "Strength",
    "Dexterity",
    "Constitution",
    "Intelligence",
    "Wisdom",
    "Charisma"
]
# Will load the Ability Score buttons into session state
for ability in ability_score_button_list:
   if st.button(ability):
      st.session_state.selected_ability = ability


# Initialising a new character sheets scores
if "new_character_sheet" not in st.session_state:
    new_character_sheet = ABILITY_SCORES_BLANK_BASE.copy()
    st.session_state.new_character_sheet = new_character_sheet


# 
if st.session_state.selected_ability is not None:
    st.write(f"Selected Ability: {st.session_state.selected_ability}")


if (st.session_state.selected_ability is not None and "scores" in st.session_state):
    selected_score = st.selectbox(
        "Choose an Ability Score",
        st.session_state.scores
    )

    if st.button("Assign Score"):
        st.session_state.new_character_sheet[st.session_state.selected_ability] = selected_score


st.write(st.session_state.new_character_sheet)


