import streamlit as st
from src.domain.models import ChatSession, Highlight, Message


# from src.services.storage import StorageService # Commented out for MVP

class AppState:
    def __init__(self):
        if "chats" not in st.session_state:
            st.session_state["chats"] = []
        if "active_chat_id" not in st.session_state:
            self.create_new_chat()
        if "scroll_target" not in st.session_state:
            st.session_state["scroll_target"] = None

    @property
    def active_chat(self) -> ChatSession:
        chat_id = st.session_state["active_chat_id"]
        return next(c for c in st.session_state["chats"] if c.id == chat_id)

    @property
    def scroll_target_id(self):
        return st.session_state["scroll_target"]

    @scroll_target_id.setter
    def scroll_target_id(self, value):
        st.session_state["scroll_target"] = value

    def create_new_chat(self):
        new_chat = ChatSession()
        st.session_state["chats"].insert(0, new_chat)
        st.session_state["active_chat_id"] = new_chat.id
        return new_chat

    def handle_new_highlight(self, text: str, msg_id: str):
        # Avoid duplicates
        if any(h.text == text for h in self.active_chat.highlights):
            return
        new_hl = Highlight(text=text, source_message_id=msg_id)
        self.active_chat.highlights.append(new_hl)
        st.rerun()

    def set_scroll_target(self, msg_id: str):
        st.session_state["scroll_target"] = msg_id

    # --- ADDED THESE METHODS ---
    def add_user_message(self, content: str):
        msg = Message(role="user", content=content)
        self.active_chat.messages.append(msg)

    def add_ai_message(self, content: str):
        msg = Message(role="assistant", content=content)
        self.active_chat.messages.append(msg)