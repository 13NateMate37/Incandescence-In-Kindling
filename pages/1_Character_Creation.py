"""
Streamlit character creation page
"""




import streamlit as st
from Stat_Array_Generation import array_Roller_Standard



# Checking whether a game has been initialised 
if not st.session_state.get("game_active", False):
    st.warning("Start a game before making character")
    st.stop()

# page title 
st.title("Character Creation")

# Storing the character name
character_name = st.text_input("Enter a name for your character")

# Subheading 
st.subheader("Ability Scores")

# Ability Score generation 
if st.button("Generate Standard Array"):
    st.session_state.scores = array_Roller_Standard()

if "scores" in st.session_state:
    st.write(st.session_state.scores)

