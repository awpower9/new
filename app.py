import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel, PeftConfig
import torch

# Load config first (lightweight)
@st.cache_resource
def get_config():
    return PeftConfig.from_pretrained("./")

# Load tokenizer (fast)
@st.cache_resource
def load_tokenizer():
    base_model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    return AutoTokenizer.from_pretrained(base_model_name)

# Main model loader (optimized caching)
@st.cache_resource(show_spinner=False)  # Disable hashing for complex objects
def load_model():
    config = get_config()
    base_model = AutoModelForCausalLM.from_pretrained(
        config.base_model_name_or_path,
        torch_dtype=torch.float16,
        device_map="auto"
    )
    return PeftModel.from_pretrained(base_model, "./")

# --- UI ---
st.title("👽 Sci-Fi Story Generator")
prompt = st.text_area("Begin your story:", "The spaceship's alarm blared...")

if st.button("Generate"):
    try:
        with st.spinner("Loading AI..."):
            model = load_model()
            tokenizer = load_tokenizer()
            
        with st.spinner("Writing..."):
            inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
            outputs = model.generate(
                **inputs,
                max_new_tokens=150,
                temperature=0.7,
                do_sample=True
            )
            story = tokenizer.decode(outputs[0], skip_special_tokens=True)
            
        st.success(story)
        
    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.info("First load may take 2-3 minutes. Please wait...")
