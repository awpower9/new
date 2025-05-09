import streamlit as st
from datetime import datetime
import base64

# Set page config
st.set_page_config(
    page_title="Cosmic Story Generator",
    page_icon="🚀",
    layout="centered"
)

# --- Custom CSS with proper space background ---
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
                        url('https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?q=80&w=1471&auto=format&fit=crop');
            background-size: cover;
            background-position: center;
            color: white;
        }
        .main {
            max-width: 700px;
            padding: 2rem;
            margin: 0 auto;
            background: rgba(0, 0, 30, 0.7);
            border-radius: 15px;
            border: 1px solid #00f7ff;
            box-shadow: 0 0 20px rgba(0, 247, 255, 0.3);
        }
        h1 {
            color: #00ffff;
            text-shadow: 0 0 10px #00ffff;
            font-family: 'Arial', sans-serif;
            text-align: center;
        }
        .subtitle {
            color: #aaa;
            text-align: center;
            margin-bottom: 2rem;
        }
        .story-box {
            background: rgba(0, 10, 20, 0.9);
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1.5rem 0;
            border-left: 3px solid #00f7ff;
        }
        .stTextInput>div>div>input {
            color: white !important;
            background: rgba(0, 20, 40, 0.8) !important;
            border: 1px solid #00f7ff !important;
        }
        .stButton>button {
            background: #00f7ff !important;
            color: black !important;
            font-weight: bold !important;
            margin: 1rem auto !important;
            display: block !important;
        }
        .save-btn {
            background: #00f7ff;
            color: black;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            text-decoration: none;
            display: inline-block;
            margin-top: 1rem;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# --- App Content ---
with st.container():
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    
    st.title("🚀 Cosmic Story Generator")
    st.markdown("<p class='subtitle'>Create your own sci-fi adventure</p>", unsafe_allow_html=True)

    prompt = st.text_input(
        "Enter your sci-fi premise:",
        placeholder="e.g. 'An AI awakens on a generation ship', 'First contact goes wrong'"
    )

    if st.button("Generate Story"):
        if not prompt.strip():
            st.warning("Please enter a sci-fi premise")
        else:
            with st.spinner('Generating your cosmic tale...'):
                # Simulate processing delay
                import time
                time.sleep(1.5)
                
                story = f"""
                **Stardate {datetime.now().strftime('%Y%m%d')} - Captain's Log**
                
                The incident began when {prompt.lower().rstrip('.')}. At first, the crew of the starship Event Horizon 
                assumed it was routine, but when the quantum scanners detected {prompt.split()[0]} readings 
                beyond known scientific parameters, we knew we'd encountered something extraordinary.
                
                "Captain, you need to see this," Science Officer Chen reported, her voice tense. "The {prompt.split()[0]} 
                phenomenon is creating a localized spacetime distortion. It's... it's like nothing in the databases."
                
                Then the transmission came through - not on any frequency we could identify, but directly into our neural implants. 
                The message was clear: "You have awakened the gateway. The test begins now."
                
                [End of log entry - continue story?]
                """
                
                st.markdown(f"<div class='story-box'>{story.strip()}</div>", unsafe_allow_html=True)

                # Download option
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"scifi_story_{timestamp}.txt"
                b64 = base64.b64encode(story.encode()).decode()
                href = f'<a href="data:file/txt;base64,{b64}" download="{filename}" class="save-btn">💾 Download Story</a>'
                st.markdown(href, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
