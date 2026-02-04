import streamlit as st
from src.state.app_state import AppState
from src.ui.sidebar_left import render_left_sidebar
from src.ui.sidebar_right import render_right_sidebar
from src.ui.chat_area import render_chat_area

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(
    page_title="PowerChat",
    layout="wide",
    initial_sidebar_state="collapsed"  # We hide the native sidebar to use our custom 3-column layout
)


# 2. Load Global CSS
def load_css():
    with open("assets/style.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# 3. Initialize Application State (Singleton)
state = AppState()


def main():
    load_css()

    # 4. The 3-Column Layout
    # We use specific ratios to create the "Command Center" look
    # Left (Nav): 1 part | Middle (Chat): 3 parts | Right (Tools): 1 part
    col_left, col_mid, col_right = st.columns([1, 3, 1], gap="small")

    # --- LEFT COLUMN (Navigation) ---
    with col_left:
        render_left_sidebar(state)

    # --- MIDDLE COLUMN (Chat Feed) ---
    with col_mid:
        # Render the history
        render_chat_area(state)

        # Render the Input Area (Sticky at bottom)
        # Note: st.chat_input automatically pins to the bottom of the container
        if prompt := st.chat_input("Type a message..."):
            # A. Add User Message
            state.add_user_message(prompt)

            # B. Mock AI Response (Placeholder for LLM Service)
            # In a real app, you'd call your service here
            import time
            time.sleep(0.5)  # Simulate network
            state.add_ai_message(f"Echo: {prompt}")

            # C. Rerun to update the UI
            st.rerun()

    # --- RIGHT COLUMN (Settings & Highlights) ---
    with col_right:
        render_right_sidebar(state)


if __name__ == "__main__":
    main()