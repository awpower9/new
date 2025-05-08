import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch  # <-- This was missing

@st.cache_resource(show_spinner="Loading AI (first time may take 2 minutes)...")
def load_model():
    model = AutoModelForCausalLM.from_pretrained(
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        torch_dtype=torch.float16,
        device_map="auto", 
        low_cpu_mem_usage=True
    )
    tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
    return model, tokenizer

# UI
st.title("🚀 Sci-Fi Story Generator")
prompt = st.text_area("Enter your prompt:", "The spaceship's alarm suddenly...")

if st.button("Generate"):
    try:
        model, tokenizer = load_model()
        with st.spinner("Writing your story..."):
            inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
            outputs = model.generate(
                **inputs,
                max_new_tokens=100,  # Reduced for stability
                temperature=0.7
            )
            story = tokenizer.decode(outputs[0], skip_special_tokens=True)
            st.success(story)
    except Exception as e:
        st.error(f"Error: {str(e)}")
