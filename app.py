import streamlit as st
from datetime import datetime
import base64

st.set_page_config(page_title="Cosmic Story Generator", page_icon="🚀", layout="centered")

# --- CSS ---
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

# --- Session State ---
if 'story' not in st.session_state:
    st.session_state.story = ""
if 'phase' not in st.session_state:
    st.session_state.phase = 'start'

# --- Header ---
st.title("🚀 Cosmic Story Generator")
st.markdown("<p class='subtitle'>Create your own sci-fi adventure</p>", unsafe_allow_html=True)

# --- PHASE: Start (Initial Input) ---
if st.session_state.phase == 'start':
    prompt = st.text_input("Enter your sci-fi premise:", placeholder="e.g. 'An AI awakens on a generation ship'", key='initial_prompt')
    if st.button("Generate Story", key='gen_btn_1'):
        if prompt.strip():
            st.session_state.story = f"""
            **Stardate {datetime.now().strftime('%Y%m%d')}**

            It began when {prompt.lower().rstrip('.')}. The starship's sensors detected anomalous readings near the {prompt.split(' ')[0]} sector.

            "Captain," Lt. Vega reported, "the quantum fluctuations are off the charts. It's like nothing we've seen before."

            Then everything changed. The last transmission before communications failed was a single repeating message: 
            "The threshold has been crossed."
            """
            st.session_state.phase = 'generated'

# --- PHASE: Generated or Continued ---
if st.session_state.phase in ['generated', 'continued']:
    st.markdown(f"<div class='story-box'>{st.session_state.story.strip()}</div>", unsafe_allow_html=True)

    # Download button
    b64 = base64.b64encode(st.session_state.story.encode()).decode()
    st.markdown(
        f'<a href="data:file/txt;base64,{b64}" download="scifi_story.txt"_
