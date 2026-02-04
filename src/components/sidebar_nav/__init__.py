import os
import streamlit as st

_COMPONENT_DIR = os.path.dirname(os.path.abspath(__file__))

def _load_file(filename):
    """Helper to read file contents as string"""
    file_path = os.path.join(_COMPONENT_DIR, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# 1. Load content
_HTML = _load_file("index.html")
_CSS = _load_file("style.css")
_JS = _load_file("script.js")

# 2. Register component
_render_nav = st.components.v2.component(
    "sidebar_nav",
    html=_HTML,
    css=_CSS,
    js=_JS,
    isolate_styles=True
)

def sidebar_nav(folders, active_chat, key="nav"):
    return _render_nav(
        key=key,
        data={"folders": folders, "active_chat": active_chat},
        on_chat_selected_change=lambda: None, # Register callback
        width="stretch"
    )