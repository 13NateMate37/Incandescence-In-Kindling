"""
Streamlit character creation page
"""



import streamlit as st

from Stat_Array_Generation import array_Roller_Standard
from Stat_Array_Generation import array_Roller_4d6d1
from Stat_Array_Generation import array_Roller_Pointbuy
from Stat_Array_Generation import ability_Score_Modifer_Calculator
from Stat_Array_Generation import ABILITY_SCORES_BLANK_BASE





# Pre load check

# Checking whether a game has been initialised 
# if not st.session_state.get("game_active", False):
#     st.warning("Start a game before making character")
#     st.stop()





# Page section 1

# 1a - Displays page title
# 1b - Displays character naming subheader
# 1c - Displays character naming input capture promt

# 1a 
st.title("Character Creation")

# 1b
st.subheader("Character Name") 

# 1c
character_name = st.text_input("Enter the chosen name here:")



# Page section 2

# 2a - Displays the Ability Score Assignment subheader
# 2b - Displays user prompt 
# 2c - Variable assignment for st.column page structure
# 2d - Structuring the idividual columns
# 2e - If there's a Stat Array in session state

# 2a
st.subheader("Ability Score Assignment")

# 2b
st.write("Choose a method to generate your Stat Array")

# 2c
ArrayButton_STD, ArrayButton_4d6, ArrayButton_PtB, = st.columns(
    3,
    width=400,
    gap="medium"
    )

# 2d
with ArrayButton_STD:
    # Loads a standard array into the session state
    if st.button("Standard"):
        st.session_state.scores = array_Roller_Standard()

with ArrayButton_4d6: 
    # Loads a 4d6d1 array into the session state
    if st.button("4d6d1"):
        st.session_state.scores = array_Roller_4d6d1()

with ArrayButton_PtB: 
    # Loads a base Pointbuy array into the session state
    if st.button("Point Buy"):
        st.session_state.scores = array_Roller_Pointbuy()

# 2e If there's a Stat Array in session state
if "scores" in st.session_state:
    # Stat_Array_Value split into columns for metric cards 
    Stat_Array_Values = st.columns(6)
    for index, score in enumerate(st.session_state.scores):
        with Stat_Array_Values[index]:
             modifierValue = ability_Score_Modifer_Calculator(score)
             st.metric(
                 label= f"Value {index + 1}",
                 value= score,
                 delta= modifierValue
                 )



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


