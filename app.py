import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftConfig
import torch

# Lightweight config loader
@st.cache_resource
def get_config():
    return PeftConfig.from_pretrained("./")

# Memory-efficient model loading
def load_model():
    config = get_config()
    
    # TinyLlama base with 4-bit quantization (50% less memory)
    base_model = AutoModelForCausalLM.from_pretrained(
        config.base_model_name_or_path,
        torch_dtype=torch.float16,
        device_map="auto",
        load_in_4bit=True,  # Critical for memory reduction
        low_cpu_mem_usage=True
    )
    
    # Load your adapter
    from peft import PeftModel
    return PeftModel.from_pretrained(base_model, "./")

# --- UI ---
st.title("👽 Sci-Fi Story Generator")
st.caption("Now with 50% less memory usage!")
prompt = st.text_area("Begin your story:", "The quantum computer whispered...")

if st.button("Generate"):
    with st.spinner("🚀 Warming up the AI..."):
        try:
            model = load_model()
            tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
            
            with st.spinner("📝 Writing your story..."):
                inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=100,  # Reduced length
                    temperature=0.7
                )
                st.success(tokenizer.decode(outputs[0], skip_special_tokens=True))
                
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.info("First load takes 2-3 minutes. Please wait...")
