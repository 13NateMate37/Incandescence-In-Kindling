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




"""
Page section 1

1a - Displays page title
1b - Displays character naming subheader
1c - Displays character naming input capture promt
"""


# 1a 
st.title("Character Creation")
# 1b
st.subheader("Character Name:") 
# 1c
character_name = st.text_input("Enter the chosen name here:")


"""
Page section 2

2a - Displays the Ability Score Assignment subheader
2b - Displays user prompt 
2c - Variable assignment for st.column page structure
2d - Structuring the idividual columns
2e - If there's a Stat Array in session state
"""


# 2a
st.subheader("Ability Score Assignment: ")
# 2b
st.write("Choose a method to generate your Stat Array")

# 2c
# Storing variables into a columns layout
ArrayButton_STD, ArrayButton_4d6, ArrayButton_PtB, = st.columns(
    3,
    width=400,
    gap="medium"
    )

# 2d

# Loads a standard array into the session state under the name score
with ArrayButton_STD:
    if st.button("Standard"):
        st.session_state.scores = array_Roller_Standard()

# Loads a 4d6d1 array into the session state under the name score
with ArrayButton_4d6: 
    if st.button("4d6d1"):
        st.session_state.scores = array_Roller_4d6d1()

# Loads a base Pointbuy array into the session state under the name score
with ArrayButton_PtB: 
    if st.button("Point Buy"):
        st.session_state.scores = array_Roller_Pointbuy()

# 2e If there's a Stat Array in session state
if "scores" in st.session_state:
    # Stat_Array_Value split into columns for metric cards 
    Stat_Array_Values = st.columns(6)
    # For each value in the stored scores
    for index, score in enumerate(st.session_state.scores):
        # Using the 6 column spaces, matching the index value of
        # scores in session state and diaplay it to the 'matching' 
        # column index as a metric card
        with Stat_Array_Values[index]:
             modifierValue = ability_Score_Modifer_Calculator(score)
             st.metric(
                 label= f"Score {index + 1}",
                 value= score,
                 delta= f"{modifierValue:+}",
                 delta_arrow= "off"
                 )


# 3a
# Setting an Ability Score that hasn't been assigned in session state to none
if "selected_ability" not in st.session_state:
    st.session_state.selected_ability = None
# 3b
# Condition to only show once an Array has been generated
if "scores" in st.session_state:
    # Prompt for user
    st.write("Assign your results to your Abilities")
# 3c
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
    # For each value in order in ability score button list
    for index, ability in enumerate(ability_score_button_list):
        # With each button,
        with Ability_Score_Buttons[index]:
            # as the button is selected,
            if st.button(ability):
                # the selection is loaded into session state 
                st.session_state.selected_ability = ability
                #   st.write("Selected:", ability)
                #   st.write("Stored value:", st.session_state.selected_ability)

# Debug inspection
# st.write(dict(st.session_state))

# Initialising a new character sheets scores
# prehaps some variable name refinement is due 
if "new_character_sheet" not in st.session_state:
    new_character_sheet = ABILITY_SCORES_BLANK_BASE.copy()
    st.session_state.new_character_sheet = new_character_sheet


# Bug checking
# st.write("Selected Ability:", st.session_state.selected_ability)
# st.write("Scores esxist:", "scores" in st.session_state)



# Visual confirmation of the Ability you're assigning to
if st.session_state.selected_ability is not None:
    st.write(f"Selected Ability: {st.session_state.selected_ability}")



# Prerequisite condition check for loading
if "scores" in st.session_state:
    # Empty list for comaprison
    already_assigned_scores = []

    # Checking if the value of an Ability is blank 
    for score in st.session_state.new_character_sheet.values():
        # If not blank,
        if score is not None:
            # Append the value to a list for comparison
            already_assigned_scores.append(score)
    # Making a copy of the original Stat Array for utilising in operations
    available_scores = st.session_state.scores.copy()
    # Dynamically updating the available scores left 
    for score in already_assigned_scores:
        available_scores.remove(score)



# Checking for a Stat Arry and a selected ability are in session state
if "scores" in st.session_state and st.session_state.selected_ability is not None:
    # Making a variable to allow for handling the changing of an already assigned value
    current_score_value = st.session_state.new_character_sheet[st.session_state.selected_ability]
    # Add the current Abilities score value back into the Array 
    if current_score_value is not None:
        available_scores.append(current_score_value)



# Dropdown menu to select a Score value from the array
if (st.session_state.selected_ability is not None and "scores" in st.session_state):
    selected_score = st.selectbox(
        "Choose an Ability Score",
        available_scores
    )
    # Visual confirmation to user
    st.write(f"Selected Value: {selected_score}")

    # Buttom to attach the Score to the Ability
    if st.button("Assign Score"):
        st.session_state.new_character_sheet[st.session_state.selected_ability] = selected_score
# st.write(st.session_state.new_character_sheet)






