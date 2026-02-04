import streamlit as st


def render_right_sidebar(state):
    # --- Top Half: Settings ---
    with st.expander("Model Parameters", expanded=True):
        st.slider("Temperature", 0.0, 1.0, 0.7, key="temp_slider")
        st.select_slider("Thinking Level", options=["Low", "High"], value="Low")

    st.divider()

    # --- Bottom Half: Highlights ---
    st.subheader("Highlights")

    if not state.active_chat.highlights:
        st.caption("Select text in the chat to pin it here.")

    # Iterate through highlights in the active chat
    for hl in state.active_chat.highlights:
        with st.container(border=True):
            # Truncate text for preview
            preview = (hl.text[:50] + '...') if len(hl.text) > 50 else hl.text
            st.markdown(f"**Ref:** `{preview}`")

            c1, c2 = st.columns([1, 1])

            # "Go" Button -> Sets scroll target
            if c1.button("Go", key=f"go_{hl.id}"):
                state.set_scroll_target(hl.source_message_id)
                st.rerun()

            # "Del" Button -> Removes highlight (Logic needed in AppState)
            if c2.button("Del", key=f"del_{hl.id}"):
                # For MVP, we just remove from list directly
                state.active_chat.highlights.remove(hl)
                st.rerun()