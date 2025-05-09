import streamlit as st
from PIL import Image

# ---- PAGE CONFIG ----
st.set_page_config(page_title="SciFi Story Generator", page_icon="🪐", layout="wide")

# ---- HEADER ----
st.markdown("""
    <style>
        body {
            background-color: #0d0c1d;
            color: #e0e0e0;
            font-family: 'Segoe UI', sans-serif;
        }
        .main-header {
            text-align: center;
            font-size: 3rem;
            font-weight: bold;
            margin-bottom: 0.5em;
            color: #00ffe1;
        }
        .sub-header {
            text-align: center;
            font-size: 1.5rem;
            margin-top: -10px;
            color: #9ae0f9;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""<div class="main-header">🪐 SciFi Story Generator</div>""", unsafe_allow_html=True)
st.markdown("""<div class="sub-header">Fuel your imagination with a cosmic tale</div>""", unsafe_allow_html=True)

# ---- BACKGROUND IMAGE (planet-themed) ----
st.image("https://images.unsplash.com/photo-1604668915841-f472c45d53c6?fit=crop&w=1920&q=80", use_column_width=True)

# ---- PROMPT INPUT ----
st.markdown("---")
st.subheader("💬 Enter a prompt to begin your story:")
prompt = st.text_input("Prompt", placeholder="e.g. A cybernetic explorer awakens in the ruins of Mars...")

# ---- GENERATE STORY (simulate for now) ----
if st.button("🚀 Generate Story"):
    if not prompt:
        st.warning("Please enter a prompt.")
    else:
        story = f"""
**Generated Story**

{prompt}

In a universe where time folds upon itself and starships bleed memory into hyperspace, your journey begins. What follows is a tale shaped by cosmic fate...
"""

        st.markdown("---")
        st.subheader("📖 Your Story")
        st.markdown(story)

        # ---- DOWNLOAD STORY ----
        st.download_button(
            label="💾 Download Story as .txt",
            data=story,
            file_name="scifi_story.txt",
            mime="text/plain"
        )
