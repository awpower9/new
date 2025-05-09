import streamlit as st
from datetime import datetime
import base64

# Set page config
st.set_page_config(
    page_title="SciFi Story Generator",
    page_icon="🛸",
    layout="centered"
)

# --- Custom CSS for a vibrant cosmic theme ---
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                        url('https://images.unsplash.com/photo-1506318137071-a8e063b4bec0?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: white;
        }
        h1 {
            color: #00ffff;
            text-shadow: 0 0 15px #00ffff;
            font-family: 'Arial', sans-serif;
        }
        .story-box {
            background: rgba(0, 0, 0, 0.7);
            padding: 2rem;
            border-radius: 15px;
            margin: 1rem 0;
            border-left: 3px solid #00f7ff;
            color: #f0f0f0;
            line-height: 1.6;
        }
        .save-button {
            background-color: #00f7ff;
            color: black;
            border: none;
            padding: 0.5rem 1.5rem;
            font-weight: bold;
            border-radius: 5px;
            margin-top: 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .save-button:hover {
            background-color: #00c4ff;
            transform: scale(1.05);
        }
        .stTextInput>div>div>input {
            color: white !important;
            background-color: rgba(0, 0, 0, 0.7) !important;
            border: 1px solid #00f7ff !important;
        }
        .stButton>button {
            background-color: #00f7ff !important;
            color: black !important;
            font-weight: bold !important;
            border: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title and Prompt ---
st.markdown("<h1 align='center'>🚀 SciFi Story Generator</h1>", unsafe_allow_html=True)
st.markdown("<p align='center' style='font-size:18px;'>Fuel your imagination with a cosmic tale</p>", unsafe_allow_html=True)

# --- User Input ---
user_prompt = st.text_input("Enter a sci-fi prompt (e.g., 'the discovery of a quantum wormhole', 'an alien AI awakening'):", "")

# --- Generate Story (Mock until model added) ---
if st.button("Generate Story", type="primary"):
    if user_prompt.strip() == "":
        st.warning("Please enter a prompt to generate your story.")
    else:
        with st.spinner('Generating your cosmic adventure...'):
            # Simulate processing delay
            import time
            time.sleep(2)
            
            story = f"""
            **Cosmic Log - Stardate {datetime.now().strftime('%Y%m%d')}**
            
            The event began when {user_prompt.lower().rstrip('.')}. At first, the science team aboard the starship Event Horizon 
            thought it was a sensor malfunction. But when the quantum distortion field expanded to 0.3 AU in diameter, 
            we knew this was something unprecedented.
            
            Commander Jax Ryland gripped the armrests of the command chair as the ship shuddered. "Report!" he barked.
            
            Lieutenant Mira Chen's fingers flew across her console. "The anomaly is generating tachyons at an increasing rate, 
            Captain. It's reacting to {user_prompt.split()[0]} like some kind of... trigger."
            
            Then the transmission came through - not on any known frequency, but directly into our minds. The message was clear: 
            "You have awakened the gateway. The test begins now."
            
            [To be continued...]
            """
            
            st.markdown(f"<div class='story-box'>{story.strip()}</div>", unsafe_allow_html=True)

            # --- Save story as text file ---
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            filename = f"sci_fi_story_{timestamp}.txt"
            b64 = base64.b64encode(story.encode()).decode()
            href = f'<a href="data:file/txt;base64,{b64}" download="{filename}" class="save-button">💾 Download Story</a>'
            st.markdown(href, unsafe_allow_html=True)
            
            st.balloons()
