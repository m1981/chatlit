import streamlit as st
from src.components.selectable_text import selectable_text


def render_chat_area(state):
    """
    Renders the middle column: The Message Feed.
    """
    st.markdown("### Current Chat")  # Header

    # 1. The Message Loop
    for msg in state.active_chat.messages:

        # Determine styling based on role
        if msg.role == "user":
            with st.chat_message("user", avatar="👤"):
                # User text is usually static, but let's make it selectable too
                st.write(msg.content)
        else:
            with st.chat_message("assistant", avatar="🤖"):
                # Check if this message is the target of a "Scroll To" action
                is_target = (state.scroll_target_id == msg.id)

                # RENDER V2 COMPONENT
                # This draws the bubble AND listens for text selection
                selection = selectable_text(
                    text=msg.content,
                    key=msg.id,
                    is_target=is_target
                )

                # Handle the event immediately
                if selection:
                    state.handle_new_highlight(selection, msg.id)

    # Reset scroll target after rendering once so it doesn't jump on every interaction
    if state.scroll_target_id:
        state.scroll_target_id = None