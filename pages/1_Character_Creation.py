"""
Streamlit character creation page
"""

import streamlit as st

if not st.session_state.get("game_active", False):
    st.warning("Start a game before making character")
    st.stop()

st.title("Character Creation")

character_name = st.text_input("Enter a name for your character")

st.subheader("Ability Scores")

st.write("Ability Score generation to go here")

