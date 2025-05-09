import streamlit as st
from datetime import datetime
import base64

# Set page config
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
    </style>
""", unsafe_allow_html=True)

# --- App Content ---
st.title("🚀 Cosmic Story Generator")
st.markdown("<p class='subtitle'>Create your own sci-fi adventure</p>", unsafe_allow_html=True)

# Initialize session state variables if they are not already present
if "story" not in st.session_state:
    st.session_state.story = ""
if "user_prompt" not in st.session_state:
    st.session_state.user_prompt = ""

# Handle user input for prompt
if st.session_state.story == "":  # Only show the input bar if no story is generated yet
    prompt = st.text_input(
        "Enter your sci-fi premise:", 
        placeholder="e.g. 'An AI awakens on a generation ship'",
        key="user_prompt"  # Ensures the input stays in session state
    )

    if st.button("Generate Story"):
        if not prompt.strip():
            st.warning("Please enter a sci-fi premise")
        else:
            with st.spinner('Generating...'):
                story = f"""
                **Stardate {datetime.now().strftime('%Y%m%d')}**
                
                It began when {prompt.lower().rstrip('.')}. The starship's sensors detected anomalous readings near the {prompt.split(' ')[0]} sector. 
                
                "Captain," Lt. Vega reported, "the quantum fluctuations are off the charts. It's like nothing we've seen before."
                
                Then everything changed. The last transmission before communications failed was a single repeating message: 
                "The threshold has been crossed."
                """
                # Append generated story to the session state
                st.session_state.story = story.strip()

                st.markdown(f"<div class='story-box'>{st.session_state.story}</div>", unsafe_allow_html=True)

                # Option to continue the story
                if st.button("Continue Story"):
                    st.session_state.story += "\n\nAnd then, the adventure continued..."
                    st.markdown(f"<div class='story-box'>{st.session_state.story}</div>", unsafe_allow_html=True)

                # Download option
                b64 = base64.b64encode(st.session_state.story.encode()).decode()
                st.markdown(
                    f'<a href="data:file/txt;base64,{b64}" download="scifi_story.txt" style="color:#00f7ff;">⬇️ Download Story</a>',
                    unsafe_allow_html=True)
else:
    # Show the previously generated story and continue option
    st.markdown(f"<div class='story-box'>{st.session_state.story}</div>", unsafe_allow_html=True)
    if st.button("Continue Story"):
        st.session_state.story += "\n\nAnd then, the adventure continued..."
        st.markdown(f"<div class='story-box'>{st.session_state.story}</div>", unsafe_allow_html=True)
        # Option to download updated story
        b64 = base64.b64encode(st.session_state.story.encode()).decode()
        st.markdown(
            f'<a href="data:file/txt;base64,{b64}" download="scifi_story.txt" style="color:#00f7ff;">⬇️ Download Story</a>',
            unsafe_allow_html=True)
