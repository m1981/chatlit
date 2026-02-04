import streamlit as st
from src.components.chat_bubble import chat_bubble
from src.core.state_manager import StateManager


def render_chat_area(state: StateManager):
    messages = state.get_messages()

    if not messages:
        st.info("No messages yet.")
        return

    with st.container(height=500):
        for msg in messages:
            result = chat_bubble(
                content=msg['content'],
                message_id=msg['id'],
                is_starred=msg['starred'],
                key=msg['id']
            )

            if result.star_clicked:
                state.toggle_star(result.star_clicked)
                st.rerun()