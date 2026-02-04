import os
import streamlit as st

# Get the directory of the current file
_COMPONENT_DIR = os.path.dirname(os.path.abspath(__file__))

def _load_file(filename):
    """Helper to read file contents as string"""
    file_path = os.path.join(_COMPONENT_DIR, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# 1. Load content from files
_HTML = _load_file("index.html")
_CSS = _load_file("style.css")
_JS = _load_file("script.js")

# 2. Register the component using V2 API (Strings only)
_render_component = st.components.v2.component(
    "chat_bubble",
    html=_HTML,
    css=_CSS,
    js=_JS,
    isolate_styles=True
)

def chat_bubble(content, message_id, is_starred=False, key=None):
    return _render_component(
        key=key,
        data={"content": content, "id": message_id, "is_starred": is_starred},
        # Register callbacks for the triggers defined in JS
        on_edit_clicked_change=lambda: None,
        on_star_clicked_change=lambda: None,
        on_more_clicked_change=lambda: None,
        width="stretch"
    )