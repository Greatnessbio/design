import streamlit as st
import io

# Function to chunk text
def chunk_text(text, chunk_size):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# Streamlit app
st.title('Text Chunker')

# File uploader
uploaded_file = st.file_uploader("Choose a .txt file", type="txt")
if uploaded_file is not None:
    # To read file as string:
    stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    
    # Slider for chunk size
    chunk_size = st.slider("Select chunk size", min_value=10, max_value=len(string_data), value=100, step=10)
    
    # Display chunks
    chunks = chunk_text(string_data, chunk_size)
    for i, chunk in enumerate(chunks):
        st.write(f"Chunk {i+1}:")
        st.text(chunk)
