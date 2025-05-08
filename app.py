import streamlit as st
from transformers import pipeline

# Ultra-simple version
st.title("🚀 Sci-Fi Generator")
prompt = st.text_area("Enter prompt:", "The time machine malfunctioned...")

if st.button("Generate"):
    with st.spinner("🤖 AI is writing..."):
        # Test with a fast small model first
        generator = pipeline("text-generation", model="distilgpt2")
        story = generator(prompt, max_length=150)[0]['generated_text']
        st.success(story)
