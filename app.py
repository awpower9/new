import streamlit as st
from datetime import datetime
import base64

# --- Session State Setup ---
if 'story' not in st.session_state:
    st.session_state.story = ""
if 'mode' not in st.session_state:
    st.session_state.mode = 'input'  # 'input', 'post_gen', 'continue'
if 'generate_button_clicked' not in st.session_state:
    st.session_state.generate_button_clicked = False

# --- Page Configuration ---
st.set_page_config(
    page_title="Cosmic Story Generator",
    page_icon="🚀",
    layout="centered"
)

# --- Custom CSS for cosmic theme ---
st.markdown("""
    <style>
        .stApp {
            background: url('https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?q=80&w=1471&auto=format&fit=crop');
            background-size: cover;
            background-position: center;
            color: white;
        }
        .main {
            max-width: 700px;
            padding: 2rem;
            margin: 0 auto;
            background: rgba(0, 0, 0, 0.7);
            border-radius: 15px;
        }
        h1 {
            color: #00ffff;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        .subtitle {
            color: #aaa;
            text-align: center;
            margin-bottom: 2rem;
        }
        .story-box {
            background: rgba(0, 0, 0, 0.8);
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1.5rem 0;
            line-height: 1.7;
            max-height: 400px;
            overflow-y: auto;
        }
        .stTextInput>div>div>input {
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            color: white !important;
            padding: 8px !important;
        }
        .stTextInput>div>div>input:focus {
            border-bottom: 2px solid #00f7ff !important;
            background: rgba(0, 247, 255, 0.1) !important;
        }
        .stButton>button {
            background: #00f7ff !important;
            color: black !important;
            border: none !important;
            width: 100%;
            margin-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title & Subtitle ---
st.title("🚀 Cosmic Story Generator")
st.markdown("<p class='subtitle'>Create your own sci-fi adventure</p>", unsafe_allow_html=True)

# --- Display Story So Far ---
if st.session_state.story:
    st.markdown(
        f"<div class='story-box'>{st.session_state.story.replace('\n', '<br>')}</div>",
        unsafe_allow_html=True
    )

# --- Initial Prompt Input ---
if st.session_state.mode == 'input':
    prompt = st.text_input("Enter your sci-fi prompt:", key="initial_input")
    if st.session_state.get("generate_button_clicked", False) == False and st.button("Generate Story"):
        st.session_state.generate_button_clicked = True
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

# --- After First Generation: Offer to Continue ---
elif st.session_state.mode == 'post_gen':
    if st.button("Continue the story?"):
        st.session_state.mode = 'continue'

# --- Continue Prompt Input ---
elif st.session_state.mode == 'continue':
    continuation = st.text_input("What happens next?", key="continue_input")
    if st.session_state.get("generate_button_clicked", False) == False and st.button("Generate Story"):
        st.session_state.generate_button_clicked = True
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

# --- Download Story Feature ---
if st.session_state.story:
    b64 = base64.b64encode(st.session_state.story.encode()).decode()
    st.markdown(
        f'<a href="data:file/txt;base64,{b64}" download="cosmic_story.txt" style="color:#00f7ff;">⬇️ Download Story</a>',
        unsafe_allow_html=True
    )
