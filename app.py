import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="AI Quote Generator",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS Injection
st.markdown("""
<style>
    /* Font Import */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,600;0,700;1,400&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Container Spacing */
    .main .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 750px;
    }

    /* Header Styling */
    .hero-title {
        background: linear-gradient(135deg, #A855F7 0%, #6366F1 50%, #3B82F6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.8rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.4rem;
        letter-spacing: -0.02em;
    }
    
    .hero-subtitle {
        color: #94A3B8;
        font-size: 1.05rem;
        text-align: center;
        margin-bottom: 2.5rem;
        font-weight: 400;
    }

    /* Full-Width Primary Button Styling */
    div.stButton > button {
        background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%);
        color: #ffffff;
        font-weight: 600;
        font-size: 1rem;
        padding: 0.65rem 1.5rem;
        border-radius: 12px;
        border: none;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.35);
        transition: all 0.25s ease;
        width: 100%;
        margin-top: 0.5rem;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.5);
        background: linear-gradient(135deg, #4F46E5 0%, #4338CA 100%);
        color: #ffffff;
    }

    /* Card Styling for Quote Output */
    .quote-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.6) 0%, rgba(15, 23, 42, 0.8) 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-left: 4px solid #6366F1;
        border-radius: 0 16px 16px 0;
        padding: 2rem;
        margin-top: 2rem;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
    }

    .quote-badge {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #818CF8;
        font-weight: 700;
        margin-bottom: 0.75rem;
    }

    .quote-text {
        font-size: 1.25rem;
        font-style: italic;
        color: #F8FAFC;
        line-height: 1.6;
        font-weight: 400;
    }
</style>
""", unsafe_allow_html=True)

# 3. Hero Header Section
st.markdown('<div class="hero-title">✨ AI Quote Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Enter a starting phrase and let the trained LSTM model weave it into a complete quote.</div>', unsafe_allow_html=True)

# 4. Form Inputs in Responsive Columns
col1, col2 = st.columns([3, 1], gap="medium")

with col1:
    prompt = st.text_input("🌱 Starting Phrase", value="are you a", placeholder="Enter initial words...")

with col2:
    length = st.number_input("🔢 Words to Add", min_value=1, max_value=100, value=15)

generate_btn = st.button("🚀 Generate Quote")

# 5. Output Card
if generate_btn or prompt:
    # Insert your model inference function here:
    # generated_quote = your_lstm_model.predict(prompt, length)
    generated_quote = f"{prompt} moment without being dragged to work toward a word to live a position that is"

    st.markdown(f"""
    <div class="quote-card">
        <div class="quote-badge">Generated Output</div>
        <div class="quote-text">"{generated_quote}"</div>
    </div>
    """, unsafe_allow_html=True)