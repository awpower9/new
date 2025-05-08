import streamlit as st
from transformers import AutoTokenizer, pipeline
import torch

# Ultra-lightweight version (no full model loading)
@st.cache_resource
def load_generator():
    return pipeline(
        "text-generation",
        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        torch_dtype=torch.float16,
        device_map="auto",
        model_kwargs={"load_in_4bit": True}  # Critical for memory
    )

st.title("🚀 Sci-Fi Story Generator")
st.image("https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif", width=200)
prompt = st.text_area("Begin your story:", "The alien transmission said...")

if st.button("Generate"):
    with st.spinner("AI is writing..."):
        try:
            generator = load_generator()
            story = generator(
                prompt,
                max_length=150,
                do_sample=True,
                temperature=0.7
            )[0]['generated_text']
            st.success(story)
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.info("First run may take 2-3 minutes to download model")
