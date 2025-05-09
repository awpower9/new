import streamlit as st
from datetime import datetime
import base64

# Set page config
st.set_page_config(
    page_title="SciFi Story Generator",
    page_icon="🛸",
    layout="centered"
)

# --- Custom CSS with Interstellar blackhole GIF background ---
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), 
                        url('https://i.gifer.com/7RtZ.gif');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
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
            background-color: rgba(0, 0, 0, 0.5);
            border-radius: 15px;
            backdrop-filter: blur(5px);
        }
        h1 {
            color: #00ffff;
            text-shadow: 0 0 10px #00ffff, 0 0 20px #0066ff;
            font-family: 'Orbitron', sans-serif;
            margin-bottom: 1.5rem;
            letter-spacing: 1px;
        }
        .subtitle {
            font-size: 1.1rem;
            margin-bottom: 2rem;
            color: #aaaaaa;
        }
        .story-box {
            background: rgba(10, 10, 30, 0.8);
            padding: 2rem;
            border-radius: 10px;
            margin: 2rem auto;
            border-left: 4px solid #00f7ff;
            box-shadow: 0 0 20px rgba(0, 247, 255, 0.3);
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
            box-shadow: 0 0 15px rgba(0, 247, 255, 0.5);
            transition: all 0.3s ease !important;
        }
        .stButton>button:hover {
            transform: scale(1.05) !important;
            box-shadow: 0 0 20px rgba(0, 247, 255, 0.8) !important;
        }
        .rocket-container {
            position: relative;
            height: 100px;
            margin: 1rem 0;
        }
        .rocket {
            font-size: 3rem;
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            animation: blast-off 1.5s ease-out forwards;
        }
        @keyframes blast-off {
            0% { transform: translate(-50%, 0) rotate(0deg); opacity: 1; }
            100% { transform: translate(-50%, -100vh) rotate(10deg); opacity: 0; }
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
            transition: all 0.3s ease;
            display: inline-block;
            box-shadow: 0 0 15px rgba(0, 247, 255, 0.5);
            text-decoration: none;
        }
        .save-button:hover {
            transform: scale(1.05);
            box-shadow: 0 0 20px rgba(0, 247, 255, 0.8);
        }
    </style>
    <link href='https://fonts.googleapis.com/css?family=Orbitron' rel='stylesheet'>
""", unsafe_allow_html=True)

# Main container
with st.container():
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    
    # Title
    st.markdown("<h1>INTERSTELLAR STORY GENERATOR</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Warp through the event horizon of creativity</p>", unsafe_allow_html=True)

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
                
                # Rocket animation
                st.markdown("""
                <div class="rocket-container">
                    <div class="rocket">🚀</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Generated story
                story = f"""
                **// STELLAR LOG - TARS Recording //**
                **Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}
                **Location:** Near Gargantua Event Horizon
                
                It started when {user_prompt.lower().rstrip('.')}. Cooper initially dismissed it as another anomaly, 
                but when the quantum fluctuations matched Murph's childhood bedroom patterns, we knew this was different.
                
                "TARS, analyze the gravitational waves," Cooper commanded, his voice tense.
                
                "Interesting," TARS responded in his calm cadence. "The {user_prompt.split()[0]} phenomenon is creating 
                a tesseract-like structure in 5-dimensional space. It appears to be... a message."
                
                Then the coordinates appeared - not on our screens, but burned into our retinas. The same coordinates 
                from 50 years ago. The same coordinates that led us here.
                
                **End of Recording**
                """
                
                st.markdown(f"<div class='story-box'>{story.strip()}</div>", unsafe_allow_html=True)

                # Download button
                timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                filename = f"interstellar_story_{timestamp}.txt"
                b64 = base64.b64encode(story.encode()).decode()
                href = f'<a href="data:file/txt;base64,{b64}" download="{filename}" class="save-button">💾 DOWNLOAD LOG ENTRY</a>'
                st.markdown(href, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
