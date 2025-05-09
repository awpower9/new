import streamlit as st
from datetime import datetime

# --- Session State Setup ---
if 'story' not in st.session_state:
    st.session_state.story = ""
if 'mode' not in st.session_state:
    st.session_state.mode = 'input'  # 'input', 'post_gen', 'continue'

st.title("🪐 Sci-Fi Story Generator")

# --- Display Story So Far ---
if st.session_state.story:
    st.markdown(
        f"""
        <div style='background-color:#111;padding:1em;border-radius:10px;
                    max-height:400px;overflow-y:scroll;color:white;margin-bottom:1em;'>
            {st.session_state.story.replace('\n', '<br>')}
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Initial Prompt Input ---
if st.session_state.mode == 'input':
    prompt = st.text_input("Enter a sci-fi prompt:", key="initial_input")
    if st.button("Generate Story"):
        if not prompt.strip():
            st.warning("Please enter a prompt!")
        else:
            new_story = f"""
**Stardate {datetime.now().strftime('%Y%m%d')}**

It began when {prompt.strip().lower()}. The signal arrived from deep space.

"Captain," Vega whispered, "this changes everything."

Reality pulsed. The universe blinked.
"""
            st.session_state.story = new_story.strip()
            st.session_state.mode = 'post_gen'
            st.experimental_rerun()

# --- After First Generation: Offer to Continue ---
elif st.session_state.mode == 'post_gen':
    if st.button("Continue the story?"):
        st.session_state.mode = 'continue'
        st.experimental_rerun()

# --- Continue Prompt Input ---
elif st.session_state.mode == 'continue':
    continuation = st.text_input("What happens next?", key="continue_input")
    if st.button("Generate Story"):
        if not continuation.strip():
            st.warning("Enter a continuation to keep going.")
        else:
            more_text = f"""
**Stardate {datetime.now().strftime('%Y%m%d')}**

Following the events, {continuation.strip().lower()} The void responded.

A shimmering gate opened. The crew stepped through... unaware of what waited beyond.
"""
            st.session_state.story += f"\n\n{more_text.strip()}"
            st.session_state.mode = 'post_gen'
            st.experimental_rerun()
