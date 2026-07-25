import streamlit as st
import tensorflow as tf
import numpy as np
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# --- Page Configuration ---
st.set_page_config(page_title="AI Quote Generator", page_icon="✨", layout="centered")

# --- Custom CSS Injection ---
st.markdown("""
    <style>
    /* Button Styling */
    .stButton>button {
        background-color: #6C63FF;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 18px;
        font-weight: 600;
        border: none;
        transition: 0.3s;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #5750D1;
        border-color: #5750D1;
        color: white;
    }
    /* Custom Quote Box */
    .quote-box {
        padding: 30px;
        background-color: #1E1E1E;
        border-left: 8px solid #6C63FF;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        font-style: italic;
        font-size: 24px;
        line-height: 1.6;
        color: #E0E0E0;
        margin-top: 30px;
        text-align: center;
    }
    /* Subtitle Styling */
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #A0A0A0;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown("<h1 style='text-align: center; color: #6C63FF;'>✨ AI Quote Generator</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Enter a starting phrase, and the trained LSTM Model will weave it into a complete quote.</div>", unsafe_allow_html=True)
st.divider()

# --- Cache Model Loading ---
@st.cache_resource
def load_assets():
    model = tf.keras.models.load_model('lstm_model.h5')
    with open('tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)
    with open('max_len.pkl', 'rb') as f:
        max_len = pickle.load(f)
        
    index_to_word = {index: word for word, index in tokenizer.word_index.items()}
    return model, tokenizer, max_len, index_to_word

try:
    model, tokenizer, max_len, index_to_word = load_assets()
except Exception as e:
    st.error(f"Error loading model files: {e}")
    st.stop()

# --- Prediction Functions ---
def predictor(model, tokenizer, text, max_len, index_to_word):
    text = text.lower()
    seq = tokenizer.texts_to_sequences([text])[0]
    if not seq:
        return ""
    seq = pad_sequences([seq], maxlen=max_len, padding='pre')
    pred = model.predict(seq, verbose=0)
    pred_index = np.argmax(pred)
    return index_to_word.get(pred_index, "")

def generate_text(model, tokenizer, seed_text, max_len, num_words, index_to_word):
    generated_text = seed_text
    for _ in range(num_words):
        next_word = predictor(model, tokenizer, generated_text, max_len, index_to_word)
        if next_word == "":
            break
        generated_text += " " + next_word
    return generated_text

# --- Interactive Layout ---
col1, col2 = st.columns([3, 1])

with col1:
    seed_text = st.text_input("🌱 Starting Phrase:", value="are you a", placeholder="Type a few words...")

with col2:
    num_words = st.number_input("🔢 Words to Add:", min_value=1, max_value=50, value=15)

st.write("") # Small spacer

# --- Generation Logic ---
if st.button("Generate Quote 🚀"):
    if not seed_text.strip():
        st.warning("Please enter a starting text prompt.")
    else:
        with st.spinner("✨ Conjuring your quote..."):
            result = generate_text(model, tokenizer, seed_text, max_len, num_words, index_to_word)
        
        # Display the stylized quote
        st.markdown(f'<div class="quote-box">"{result}"</div>', unsafe_allow_html=True)