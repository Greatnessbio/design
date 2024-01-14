import streamlit as st
import io
import os

# Function to chunk text
def chunk_text(text, chunk_size):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# Function to convert bytes to KB or MB
def convert_size(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} bytes"
    size_kb = size_bytes / 1024
    if size_kb < 1024:
        return f"{size_kb:.2f} KB"
    size_mb = size_kb / 1024
    return f"{size_mb:.2f} MB"

# Streamlit app
st.title('Text Chunker with Downloadable Chunks')

# File uploader
uploaded_file = st.file_uploader("Choose a .txt file", type="txt")
if uploaded_file is not None:
    # To read file as string:
    stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    
    # Slider for chunk size in KB or MB
    chunk_size_kb = st.slider("Select chunk size (KB)", min_value=1, max_value=int(len(string_data)/1024), value=10, step=1)
    chunk_size = chunk_size_kb * 1024  # Convert KB to bytes
    
    # Display chunks and provide download links
    chunks = chunk_text(string_data, chunk_size)
    for i, chunk in enumerate(chunks):
        st.write(f"Chunk {i+1} ({convert_size(len(chunk))}):")
        st.download_button(label=f"Download Chunk {i+1}",
                           data=chunk,
                           file_name=f"{os.path.splitext(uploaded_file.name)[0]}_{i+1}.txt",
                           mime="text/plain")
