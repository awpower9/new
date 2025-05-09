import streamlit as st
from datetime import datetime
import base64

# --- Page Config ---
st.set_page_config(
    page_title="Cosmic Story Generator",
    page_icon="🚀",
    layout="centered"
)

# --- Custom CSS ---
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

# --- Initialize Session State ---
if 'story' not in st.session_state:
    st.session_state.story = ""
if 'mode' not in st.session_state:
    st.session_state.mode = 'input'  # 'input', 'post_gen', 'continue'

# --- Title & Subtitle ---
st.title("🚀 Cosmic Story Generator")
st.markdown("<p class='subtitle'>Create your own sci-fi adventure</p>", unsafe_allow_html=True)

# --- Show story if any ---
if st.session_state.story:
    st.markdown(f"<div class='story-box'>{st.session_state.story.strip()}</div>", unsafe_allow_html=True)

# --- Input Mode ---
if st.session_state.mode == 'input':
    prompt = st.text_input("Enter your sci-fi premise:", placeholder="e.g. 'An AI awakens on a generation ship'", key="initial_prompt")
    if st.button("Generate Story", key="gen1"):
        if not prompt.strip():
            st.warning("Please enter a sci-fi premise")
        else:
            story = f"""
            **Stardate {datetime.now().strftime('%Y%m%d')}**

            It began when {prompt.lower().rstrip('.')}. The starship's sensors detected anomalous readings near the {prompt.split(' ')[0]} sector.

            "Captain," Lt. Vega reported, "the quantum fluctuations are off the charts. It's like nothing we've seen before."

            Then everything changed. The last transmission before communications failed was a single repeating message:
            "The threshold has been crossed."
            """
            st.session_state.story += f"\n\n{story.strip()}"
            st.session_state.mode = 'post_gen'
            st.experimental_rerun()

# --- After Generation: Ask to Continue ---
elif st.session_state.mode == 'post_gen':
    if st.button("Continue Story?", key="ask_continue"):
        st.session_state.mode = 'continue'
        st.experimental_rerun()

# --- Continue Mode ---
elif st.session_state.mode == 'continue':
    prompt = st.text_input("Add your next input to continue the story:", key="continue_prompt")
    if st.button("Generate Story", key="gen_continue"):
        if not prompt.strip():
            st.warning("Please enter something to continue the story.")
        else:
            story = f"""
            **Stardate {datetime.now().strftime('%Y%m%d')}**

            Building upon the events, {prompt.lower().rstrip('.')}. The ship's AI, now partially sentient, began interpreting the signals not as threats, but as a warning.

            Deep within the neural networks, a message emerged: "Humanity must choose: evolve or perish."

            The crew stared into the abyss of the unknown, knowing only one thing — the journey had just begun.
            """
            st.session_state.story += f"\n\n{story.strip()}"
            st.session_state.mode = 'post_gen'
            st.experimental_rerun()

# --- Download Link ---
if st.session_state.story:
    b64 = base64.b64encode(st.session_state.story.encode()).decode()
    st.markdown(
        f'<a href="data:file/txt;base64,{b64}" download="scifi_story.txt" style="color:#00f7ff;">⬇️ Download Story</a>',
        unsafe_allow_html=True
    )
