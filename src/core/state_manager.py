import streamlit as st


class StateManager:
    def __init__(self):
        self._init_defaults()

    def _init_defaults(self):
        # Initialize Folders
        if "folders" not in st.session_state:
            st.session_state.folders = {
                "Work Projects": ["Q3 Report", "Debug Script"],
                "Personal": ["Japan Trip", "Recipes"],
                "Archive": ["2023 Notes"]
            }

        # Initialize Chat History
        if "chat_history" not in st.session_state:
            # Pre-fill some dummy data for the demo
            st.session_state.chat_history = {
                "Q3 Report": [{"id": "1", "role": "assistant", "content": "Hello!", "starred": False}],
                "Debug Script": [],
                "Japan Trip": [],
                "Recipes": [],
                "2023 Notes": []
            }

        if "current_chat_id" not in st.session_state:
            st.session_state.current_chat_id = "Q3 Report"

    @property
    def current_chat_id(self):
        return st.session_state.current_chat_id

    @current_chat_id.setter
    def current_chat_id(self, chat_id):
        st.session_state.current_chat_id = chat_id

    def get_folders(self):
        """Returns the folder structure for the sidebar component"""
        return st.session_state.folders

    def get_messages(self):
        if not self.current_chat_id:
            return []
        return st.session_state.chat_history.get(self.current_chat_id, [])

    def add_message(self, role, content, attachments=None):
        if not self.current_chat_id:
            return

        msg = {
            "id": f"{self.current_chat_id}_{len(self.get_messages())}",
            "role": role,
            "content": content,
            "attachments": attachments or [],
            "starred": False
        }
        st.session_state.chat_history[self.current_chat_id].append(msg)

    def toggle_star(self, message_id):
        # Simple toggle logic
        msgs = self.get_messages()
        for m in msgs:
            if m['id'] == message_id:
                m['starred'] = not m['starred']
                break