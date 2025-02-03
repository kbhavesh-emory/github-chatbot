# app.py
import streamlit as st
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import os

# Load FAISS index and embeddings
repo_name = "digital_slide_archive"  # Example repo
index = faiss.read_index(os.path.join("data", repo_name, "index.faiss"))
with open(os.path.join("data", repo_name, "extracted_text.txt"), "r", encoding="utf-8") as f:
    text_data = f.read().split("\n")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Streamlit app
st.title("GitHub Repo Chatbot")
query = st.text_input("Ask a question:")

if query:
    # Generate query embedding
    query_embedding = model.encode(query)
    
    # Search FAISS index
    distances, indices = index.search(np.array([query_embedding]), k=5)
    
    # Display results
    st.write("Top results:")
    for idx in indices[0]:
        st.write(text_data[idx])