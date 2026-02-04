import streamlit as st


def render_left_sidebar(state):
    if st.button("+ New Chat", use_container_width=True):
        state.create_new_chat()
        st.rerun()

    st.markdown("### History")
    for chat in st.session_state["chats"]:
        # Simple button for each chat
        label = chat.title if len(chat.title) < 20 else chat.title[:17] + "..."
        if st.button(label, key=f"nav_{chat.id}", use_container_width=True):
            st.session_state["active_chat_id"] = chat.id
            st.rerun()