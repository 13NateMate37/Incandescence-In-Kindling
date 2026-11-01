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
st.subheader("Character Name:") 

# 1c
character_name = st.text_input("Enter the chosen name here:")



# Page section 2

# 2a - Displays the Ability Score Assignment subheader
# 2b - Displays user prompt 
# 2c - Variable assignment for st.column page structure
# 2d - Structuring the idividual columns
# 2e - If there's a Stat Array in session state

# 2a
st.subheader("Ability Score Assignment: ")

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
    # Loads a standard array into the session state under the name score
    if st.button("Standard"):
        st.session_state.scores = array_Roller_Standard()

with ArrayButton_4d6: 
    # Loads a 4d6d1 array into the session state under the name score
    if st.button("4d6d1"):
        st.session_state.scores = array_Roller_4d6d1()

with ArrayButton_PtB: 
    # Loads a base Pointbuy array into the session state under the name score
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
                 label= f"Score {index + 1}",
                 value= score,
                 delta= f"{modifierValue:+}",
                 delta_arrow= "off"
                 )



# Settin an Ability Score that hasn't been assigned in s
# ession state to none
if "selected_ability" not in st.session_state:
    st.session_state.selected_ability = None

# Condition to only show once an Array has been generated
if "scores" in st.session_state:
    # Prompt for user
    st.write("Assign your results to your Abilities")

# List to loop through for buttons
ability_score_button_list = [
    "Strength",
    "Dexterity",
    "Constitution",
    "Intelligence",
    "Wisdom",
    "Charisma"
]
# Structuring the button layout
Ability_Score_Buttons = st.columns(6)
# Condition to only show once an Array has been generated
if "scores" in st.session_state:
    # Will load the Ability Score buttons into session state
    for index, ability in enumerate(ability_score_button_list):
        with Ability_Score_Buttons[index]:
            if st.button(ability):
                st.session_state.selected_ability = ability
                #   st.write("Selected:", ability)
                #   st.write("Stored value:", st.session_state.selected_ability)

# Debug inspection
# st.write(dict(st.session_state))

# Initialising a new character sheets scores
if "new_character_sheet" not in st.session_state:
    new_character_sheet = ABILITY_SCORES_BLANK_BASE.copy()
    st.session_state.new_character_sheet = new_character_sheet


# Bug checking
# st.write("Selected Ability:", st.session_state.selected_ability)
# st.write("Scores esxist:", "scores" in st.session_state)



# Visual confirmation of the Ability you're assigning to
if st.session_state.selected_ability is not None:
    st.write(f"Selected Ability: {st.session_state.selected_ability}")




# Dropdown menu to select a Score value from the array
if (st.session_state.selected_ability is not None and "scores" in st.session_state):
    selected_score = st.selectbox(
        "Choose an Ability Score",
        st.session_state.scores
    )
    st.write(f"Selected Value: {selected_score}")

    # Buttom to attached the Score to the Ability
    if st.button("Assign Score"):
        st.session_state.new_character_sheet[st.session_state.selected_ability] = selected_score
# st.write(st.session_state.new_character_sheet)




# Prerequisite condition check for loading
if "scores" in st.session_state:
    # Empty list for comaprison
    already_assigned_scores = []

    # Checking 
    for score in st.session_state.new_character_sheet.values():
        if score is not None:
            already_assigned_scores.append(score)

    available_scores = st.session_state.scores.copy()

    for score in already_assigned_scores:
        available_scores.remove(score)


if "scores" in st.session_state and st.session_state.selected_ability is not None:
    current_score_value = st.session_state.new_character_sheet[st.session_state.selected_ability]

    if current_score_value is not None:
        available_scores.append(current_score_value)