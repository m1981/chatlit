import streamlit as st
from src.core.state_manager import StateManager
from src.services.ai_service import AIService


def render_input_area(state: StateManager):
    col_plus, col_input = st.columns([0.05, 0.95])

    with col_plus:
        with st.popover("➕", use_container_width=True):
            files = st.file_uploader("Attach", accept_multiple_files=True)

    with col_input:
        prompt = st.chat_input("Message...")

    if prompt:
        # 1. Update State (User)
        state.add_message("user", prompt, files)

        # 2. Call Service
        response_text = AIService.generate_response(prompt, files)

        # 3. Update State (AI)
        state.add_message("assistant", response_text)

        st.rerun()