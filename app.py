"""
Streamlit Home Page
"""

import streamlit as st

# Page details
st.set_page_config(
    page_title= "IncandEssence",
    page_icon= "\U0001F3B2",
    layout= "wide"
)

# Initialising a game state
if "game_active" not in st.session_state:
    st.session_state.game_active = False


st.title("Essence Coalesses")

if not st.session_state.game_active:
    st.subheader("Main Menu")

    if st.button("New Game"):
        st.session_state.game_active = True

        st.rerun()

else:
    st.subheader("Game Menu")
    st.write("Game session active.")

    if st.button("Create Character"):
        st.switch_page("pages/1_Character_Creation.py")

