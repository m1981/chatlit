import streamlit as st
from src.core.state_manager import StateManager
from src.ui.sidebar import render_sidebar
from src.ui.chat_area import render_chat_area
from src.ui.input_area import render_input_area

# 1. Config
st.set_page_config(page_title="Enterprise Chat", layout="wide")

# 2. Initialize State
state = StateManager()

# 3. Render Layout
render_sidebar(state)

if state.current_chat_id:
    st.title(f"Chat: {state.current_chat_id}")
    render_chat_area(state)
    render_input_area(state)
else:
    st.header("Welcome")
    st.write("Please select or create a chat.")