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
            background-image: url('https://www.pexels.com/photo/blue-universe-956981/');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: white;
        }
        h1 {
            color: #00ffff;
            text-shadow: 0 0 15px #00ffff;
        }
        .story-box {
            background: rgba(0, 0, 0, 0.6);
            padding: 1.5rem;
            border-radius: 10px;
            margin-top: 1rem;
            box-shadow: 0 0 25px #00f7ff;
        }
        .save-button {
            background-color: #00f7ff;
            color: black;
            border: none;
            padding: 0.5rem 1rem;
            font-weight: bold;
            border-radius: 5px;
            margin-top: 1rem;
            text-decoration: none;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title and Prompt ---
st.markdown("<h1 align='center'>🚀 SciFi Story Generator</h1>", unsafe_allow_html=True)
st.markdown("<p align='center'>Fuel your imagination with a cosmic tale</p>", unsafe_allow_html=True)

# --- User Input ---
user_prompt = st.text_input("Enter a sci-fi prompt:", "")

# --- Generate Story (Mock until model added) ---
if st.button("Generate Story"):
    if user_prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        story = f"""
        In a distant quadrant of the Andromeda galaxy, {user_prompt} became the catalyst for humanity’s greatest leap...
        (✨ Your model-generated story would continue here ✨)
        """
        st.markdown(f"<div class='story-box'><pre>{story.strip()}</pre></div>", unsafe_allow_html=True)

        # --- Save story as text file ---
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"sci_story_{timestamp}.txt"
        b64 = base64.b64encode(story.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="{filename}" class="save-button">💾 Save Story</a>'
        st.markdown(href, unsafe_allow_html=True)
