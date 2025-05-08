import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

@st.cache_resource(show_spinner="Loading AI (first time may take 5 minutes)...")
def load_model():
    model = AutoModelForCausalLM.from_pretrained(
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        torch_dtype=torch.float32,  # Changed to float32 for CPU
        device_map="cpu",  # Force CPU usage
        low_cpu_mem_usage=True
    )
    tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
    return model, tokenizer

# UI
st.title("🚀 Sci-Fi Story Generator (CPU Version)")
prompt = st.text_area("Enter your prompt:", "The alien message decoded to...")

if st.button("Generate"):
    try:
        model, tokenizer = load_model()
        with st.spinner("Writing your story (may be slow on CPU)..."):
            inputs = tokenizer(prompt, return_tensors="pt")  # Removed .to("cuda")
            outputs = model.generate(
                **inputs,
                max_new_tokens=75,  # Reduced further for CPU
                temperature=0.7
            )
            story = tokenizer.decode(outputs[0], skip_special_tokens=True)
            st.success(story)
    except Exception as e:
        st.error(f"Error: {str(e)}")
