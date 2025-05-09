import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="Sci-Fi Story Generator", page_icon="🪐", layout="wide")

# Load Lottie animation from URL
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_space = load_lottie_url("https://assets3.lottiefiles.com/packages/lf20_kyu7xb1v.json")

# ---- SIDEBAR ----
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3917/3917688.png", width=100)
    st.title("🧠 StoryCraft AI")
    st.markdown("🚀 Generate epic **Sci-Fi stories** trained on 50+ books.\n\nCrafted using Deep Learning, Streamlit, and Sci-Fi magic.")
    st.markdown("---")
    st.markdown("Made with 💙 by [Your Name]")

# ---- HEADER ----
st.markdown("<h1 style='text-align: center; color: #00ffee;'>🪐 Sci-Fi Story Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 20px;'>Where Artificial Intelligence meets Interstellar Imagination.</p>", unsafe_allow_html=True)

# ---- MAIN INPUT ----
with st.container():
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("⚙️ Prompt Settings")
        genre = st.selectbox("Choose your Sci-Fi subgenre", ["Space Opera", "Cyberpunk", "Time Travel", "Post-Apocalyptic", "Alien Invasion"])
        protagonist = st.text_input("👤 Main Character's Name", value="Nova Solaris")
        mood = st.slider("🌌 Story Mood", 0, 100, 70)
        st.markdown("🔧 Model Status: `Offline` (Demo Mode)")

    with col2:
        st_lottie(lottie_space, height=300, key="space")

# ---- GENERATE STORY (Placeholder) ----
st.markdown("---")
st.subheader("📖 Your Generated Story")

if st.button("Generate"):
    st.success("✨ Story Generated!")
    st.markdown(f"""
    **Title:** *{genre} Chronicles: The Rise of {protagonist}*

    In a world where stardust veins pulse through machines and forgotten ruins orbit black suns, **{protagonist}** awakens in a derelict satellite. Humanity’s last hope, equipped with a memory that isn’t theirs and a mission older than time.

    As cybernetic storms brew over the neon rings of Jupiter, whispers of rebellion echo through the void...

    *(The rest of your galactic tale continues...)*  
    """)
else:
    st.warning("⬅️ Fill in the details and click Generate")

# ---- FOOTER ----
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>© 2025 StoryCraft AI — Powered by Deep Learning & Galactic Imagination</p>", unsafe_allow_html=True)
