import streamlit as st
from src.core.state_manager import StateManager
from src.components.sidebar_nav import sidebar_nav


def render_sidebar(state: StateManager):
    with st.sidebar:
        st.title("🗂️ Workspace")

        # New Chat Button (Standard Streamlit is fine for simple buttons)
        if st.button("➕ New Chat", use_container_width=True, type="primary"):
            # Logic to create new chat would go here
            pass

        st.markdown("---")

        # --- CUSTOM COMPONENT RENDERING ---
        # We pass the folder structure and the currently active chat ID
        result = sidebar_nav(
            folders=state.get_folders(),
            active_chat=state.current_chat_id,
            key="main_nav"
        )

        # --- HANDLE EVENTS ---
        if result.chat_selected:
            # If the user clicked a chat in the custom component, update state
            if result.chat_selected != state.current_chat_id:
                state.current_chat_id = result.chat_selected
                st.rerun()

        st.markdown("---")
        with st.expander("⚙️ Settings"):
            st.write("User: Admin")
            st.write("Version: 2.0.0")