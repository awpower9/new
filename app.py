import streamlit as st
from datetime import datetime
import base64

# Set page config
st.set_page_config(
    page_title="Sci-fi Story Generator",
    page_icon="🌌",
    layout="centered"
)

# --- Custom CSS with static Interstellar background ---
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), 
                        url('https://wallpapercave.com/wp/wp9414530.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: white;
            min-height: 100vh;
        }
        .main {
            max-width: 700px;
            width: 100%;
            padding: 2rem;
            margin: 0 auto;
            text-align: center;
            background-color: rgba(0, 0, 0, 0.7);
            border-radius: 15px;
            border: 1px solid rgba(0, 247, 255, 0.3);
            box-shadow: 0 0 30px rgba(0, 247, 255, 0.2);
        }
        h1 {
            color: #00ffff;
            text-shadow: 0 0 10px #00ffff;
            font-family: 'Orbitron', sans-serif;
            margin-bottom: 1rem;
            letter-spacing: 2px;
        }
        .subtitle {
            font-size: 1.1rem;
            margin-bottom: 2rem;
            color: #aaaaaa;
            font-style: italic;
        }
        .story-box {
            background: rgba(10, 10, 30, 0.9);
            padding: 2rem;
            border-radius: 10px;
            margin: 2rem auto;
            border-left: 4px solid #00f7ff;
            box-shadow: 0 0 25px rgba(0, 247, 255, 0.2);
            color: #f0f0f0;
            line-height: 1.7;
            text-align: left;
        }
        .stTextInput>div>div>input {
            color: white !important;
            background-color: rgba(0, 10, 20, 0.8) !important;
            border: 1px solid #00f7ff !important;
            border-radius: 5px !important;
            padding: 10px !important;
        }
        .stButton>button {
            background: linear-gradient(135deg, #00f7ff, #0066ff) !important;
            color: black !important;
            font-weight: bold !important;
            border: none !important;
            border-radius: 5px !important;
            padding: 10px 25px !important;
            margin: 1.5rem auto !important;
            transition: all 0.3s ease !important;
        }
        .stButton>button:hover {
            transform: scale(1.05) !important;
            box-shadow: 0 0 15px rgba(0, 247, 255, 0.7) !important;
        }
        .save-button {
            background: linear-gradient(135deg, #00f7ff, #0066ff);
            color: black;
            border: none;
            padding: 0.7rem 1.8rem;
            font-weight: bold;
            border-radius: 5px;
            margin: 1.5rem auto;
            cursor: pointer;
            display: inline-block;
            text-decoration: none;
        }
        .rocket-icon {
            font-size: 2rem;
            display: inline-block;
            animation: float 3s ease-in-out infinite;
        }
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
    </style>
    <link href='https://fonts.googleapis.com/css?family=Orbitron' rel='stylesheet'>
""", unsafe_allow_html=True)

# Main container
with st.container():
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    
    # Title with floating rocket
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: center; gap: 15px;">
            <h1>SCI-FI STORY GENERATOR</h1>
            <div class="rocket-icon">🚀</div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>\"We used to look up at the sky and wonder...\"</p>", unsafe_allow_html=True)

    # User Input
    user_prompt = st.text_input(
        "", 
        placeholder="Enter your sci-fi prompt (e.g. 'The wormhole near Saturn begins transmitting', 'Murph discovers the quantum data')",
        key="prompt_input"
    )

    # Generate Story
    if st.button("ENGAGE WARP DRIVE", key="generate_button"):
        if not user_prompt.strip():
            st.warning("⚠️ Singularity detected! Please enter a prompt.")
        else:
            with st.spinner('Bending spacetime continuum...'):
                import time
                time.sleep(2)
                
                # Generated story
                story = f"""
                **// STELLAR LOG - TARS Recording //**
                **Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}
                **Location:** Near Gargantua Event Horizon
                
                It started when {user_prompt.lower().rstrip('.')}. Cooper initially dismissed it as instrument error, 
                but when the quantum fluctuations matched the gravitational anomalies from Miller's planet, 
                we knew this was different.
                
                "TARS, set humor to 75% and analyze," Cooper commanded.
                
                "Well, this is awkward," TARS responded. "The {user_prompt.split()[0]} phenomenon appears to be 
                manipulating spacetime in ways that violate all known physics. On the bright side, 
                I'm now 75% more amusing."
                
                Then the message appeared - not in any language, but as gravitational ripples in the fabric 
                of spacetime itself. The coordinates pointed back to Earth. Back to Murph.
                
                **End of Recording**
                """
                
                st.markdown(f"<div class='story-box'>{story.strip()}</div>", unsafe_allow_html=True)

                # Download button
                timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                filename = f"sci-fi_story_{timestamp}.txt"
                b64 = base64.b64encode(story.encode()).decode()
                href = f'<a href="data:file/txt;base64,{b64}" download="{filename}" class="save-button">💾 DOWNLOAD LOG ENTRY</a>'
                st.markdown(href, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
