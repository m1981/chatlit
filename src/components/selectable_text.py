import streamlit as st

# Inline JS for simplicity in MVP
_JS = """
export default function(component) {
    const { setTriggerValue, data, parentElement } = component;

    // 1. Render Text
    // We use a simple div. In production, you might want a Markdown renderer here.
    if (!parentElement.querySelector('.content')) {
        const div = document.createElement('div');
        div.className = 'content';
        div.style.whiteSpace = 'pre-wrap'; // Preserve formatting
        div.innerText = data.text; // Safe injection
        parentElement.appendChild(div);

        // 2. Listen for Selection
        div.onmouseup = () => {
            const selection = window.getSelection();
            const text = selection.toString();
            if (text.length > 0) {
                setTriggerValue('selection', text);
            }
        };
    }

    // 3. Handle Scroll Target
    if (data.is_target) {
        parentElement.scrollIntoView({behavior: "smooth", block: "center"});
        parentElement.style.backgroundColor = "rgba(255, 255, 0, 0.2)";
        setTimeout(() => parentElement.style.backgroundColor = "transparent", 1500);
    }
}
"""

_component = st.components.v2.component(
    "selectable_text",
    js=_JS,
    isolate_styles=False  # Inherit Streamlit styles
)


def selectable_text(text: str, key: str, is_target: bool = False):
    """
    Renders text and returns selected string if any.
    """
    return _component(
        key=key,
        data={"text": text, "is_target": is_target},
        on_selection_change=lambda: None  # Register trigger
    )