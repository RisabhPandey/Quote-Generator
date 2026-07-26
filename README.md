# ✨ AI Quote Generator (LSTM)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://quote-generator-using-lstm.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=flat&logo=TensorFlow&logoColor=white)](https://www.tensorflow.org/)

An interactive, AI-powered web application that generates complete, thought-provoking quotes based on a user-provided starting phrase. Built with a custom Long Short-Term Memory (LSTM) neural network and a modern, glassmorphism-styled Streamlit interface.

**🔗 Live Demo:** [AI Quote Generator](https://quote-generator-using-lstm.streamlit.app/)  
**📂 GitHub Repository:** [RisabhPandey/Quote-Generator](https://github.com/RisabhPandey/Quote-Generator)

---

## 🚀 Features
* **Deep Learning Model:** Powered by a sequential LSTM network trained on a dataset of famous quotes.
* **Dynamic Text Generation:** Predicts the next word iteratively to weave a cohesive sentence.
* **Modern UI:** Features a sleek, responsive design with a gradient glassmorphism aesthetic and smooth hover animations.
* **Customizable Output:** Users can control the exact number of words to generate.

---

## 🧠 Model Architecture

The text generation model was built using **TensorFlow/Keras** with the following pipeline:
1. **Text Preprocessing:** Lowercasing, punctuation removal, and tokenization using the Keras `Tokenizer` (Vocabulary Size: ~8,978 words).
2. **Padding:** Sequences were pre-padded to ensure a uniform length (Max Length: 745).
3. **Sequential Network:**   
   * `Embedding Layer`: Converts word indices into dense vectors of fixed size (50 dimensions).   
   * `LSTM Layer`: 128 units to capture long-term dependencies and context.   
   * `Dense Layer`: Output layer with a `softmax` activation function to predict the probability distribution of the next word in the vocabulary.

---

## 📂 Project Structure
```text
📦 Quote-Generator
 ┣ 📂 .streamlit
 ┃ ┗ 📜 config.toml          # Streamlit UI theme configuration
 ┣ 📜 app.py                 # Main Streamlit web application script
 ┣ 📜 lstm_model.h5          # Trained TensorFlow/Keras model
 ┣ 📜 tokenizer.pkl          # Saved vocabulary tokenizer
 ┣ 📜 max_len.pkl            # Saved maximum sequence length integer
 ┣ 📜 word_pred.ipynb        # Jupyter Notebook with training code
 ┗ 📜 requirements.txt       # Python dependencies
```

---

## 💻 Local Installation & Setup
To run this project on your local machine, follow these steps:

**1. Clone the repository**
```bash
git clone https://github.com/RisabhPandey/Quote-Generator.git
cd Quote-Generator
```

**2. Create and activate a virtual environment**

On Windows:
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

On macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Install the dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the Streamlit app**
```bash
python -m streamlit run app.py
```

**5. View the app**
Open your web browser and navigate to `http://localhost:8501`.

---

## 🛠️ Tech Stack
* **Machine Learning:** TensorFlow, Keras
* **Data Processing:** NumPy, Pandas, Pickle
* **Web Framework:** Streamlit
* **Styling:** Custom CSS, HTML
