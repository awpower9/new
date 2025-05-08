import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch

# 1. Load base model (TinyLlama) - cached after first load
@st.cache_resource(show_spinner="Loading AI brain (one-time setup)...")
def load_base_model():
    return AutoModelForCausalLM.from_pretrained(
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        torch_dtype=torch.float16,
        device_map="auto"
    )

# 2. Load your adapter - cached
@st.cache_resource
def load_adapter(base_model):
    return PeftModel.from_pretrained(base_model, "./")

# 3. Load tokenizer - cached
@st.cache_resource
def load_tokenizer():
    return AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")

# --- UI ---
st.title("👽 Your Sci-Fi Story Generator")
st.image("https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif", width=200)
prompt = st.text_area("Begin your story:", "The alien artifact began to...")

if st.button("Generate Story"):
    try:
        # Load everything with progress bars
        with st.spinner("Loading base model..."):
            base_model = load_base_model()
        
        with st.spinner("Applying your sci-fi training..."):
            model = load_adapter(base_model)
        
        tokenizer = load_tokenizer()

        # Generate story
        with st.spinner("Writing your story..."):
            inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
            outputs = model.generate(
                **inputs,
                max_new_tokens=200,
                temperature=0.7
            )
            story = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        st.success(story)
        st.download_button("Download Story", story, file_name="sci-fi-story.txt")
    
    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.info("Check if all model files are uploaded correctly!")
