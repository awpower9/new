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
        }
        /* Remove all input borders and styling */
        .stTextInput>div>div>input {
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            color: white !important;
            padding: 8px !important;
        }
        /* Add subtle underline instead */
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

# --- App Content ---
st.title("🚀 Cosmic Story Generator")
st.markdown("<p class='subtitle'>Create your own sci-fi adventure</p>", unsafe_allow_html=True)

# Initialize session state variables if they don't exist
if 'story' not in st.session_state:
    st.session_state.story = ""
if 'prompt' not in st.session_state:
    st.session_state.prompt = ""
if 'generated' not in st.session_state:
    st.session_state.generated = False

# Input prompt (visible only if no story is generated yet)
if not st.session_state.generated:
    prompt = st.text_input(
        "Enter your sci-fi premise:", 
        value=st.session_state.prompt,
        placeholder="e.g. 'An AI awakens on a generation ship'"
    )
else:
    prompt = st.session_state.prompt  # Retain the prompt if a story exists

# Generate story button
if st.button("Generate Story") and prompt.strip():
    with st.spinner('Generating...'):
        # Generate a new story based on the prompt
        st.session_state.story = f"""
        **Stardate {datetime.now().strftime('%Y%m%d')}**
        
        It began when {prompt.lower().rstrip('.')}. The starship's sensors detected anomalous readings near the {prompt.split(' ')[0]} sector. 
        
        "Captain," Lt. Vega reported, "the quantum fluctuations are off the charts. It's like nothing we've seen before."
        
        Then everything changed. The last transmission before communications failed was a single repeating message: 
        "The threshold has been crossed."
        """
        st.session_state.prompt = prompt  # Save the prompt to session state
        st.session_state.generated = True  # Mark the story as generated

# Display the story if it exists
if st.session_state.story:
    st.markdown(f"<div class='story-box'>{st.session_state.story.strip()}</div>", unsafe_allow_html=True)
    
    # Download option
    b64 = base64.b64encode(st.session_state.story.encode()).decode()
    st.markdown(
        f'<a href="data:file/txt;base64,{b64}" download="scifi_story.txt" style="color:#00f7ff;">⬇️ Download Story</a>',
        unsafe_allow_html=True
    )
    
    # Continue the story button (appears after the first story is generated)
    continuation = st.text_input("Add to the story:", placeholder="Continue the adventure...")
    
    # When user provides a continuation, append it to the story
    if continuation.strip():
        st.session_state.story += f"\n\n{continuation.strip()}"
        st.session_state.prompt = continuation.strip()  # Update the prompt for future continuation

    # "Generate New Story" button (replaces "Generate Story" and "Continue the Story" after the first generation)
    if st.session_state.generated:
        generate_new_button = st.button("Generate New Story")
        if generate_new_button:
            # Reset everything for a new story generation
            st.session_state.story = ""
            st.session_state.prompt = ""
            st.session_state.generated = False
