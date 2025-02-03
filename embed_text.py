# embed_text.py
from sentence_transformers import SentenceTransformer
import numpy as np
import os

def embed_text(text):
    """
    Generate embeddings for the input text.
    """
    model = SentenceTransformer("all-MiniLM-L6-v2")
    # Split text into sentences or chunks for better embeddings
    sentences = text.split("\n")
    sentences = [s.strip() for s in sentences if s.strip()]
    embeddings = model.encode(sentences)
    return embeddings

if __name__ == "__main__":
    repo_name = "digital_slide_archive"  # Example repo
    text_file = os.path.join("data", repo_name, "extracted_text.txt")
    
    if not os.path.exists(text_file):
        print(f"Error: {text_file} does not exist. Run clone_repos.py first.")
    else:
        try:
            with open(text_file, "r", encoding="utf-8") as f:
                text_data = f.read()
            
            if not text_data:
                print(f"Error: {text_file} is empty.")
            else:
                # Generate embeddings
                embeddings = embed_text(text_data)
                if embeddings.size == 0:
                    print("Error: No embeddings generated. Check the input text.")
                else:
                    np.save(os.path.join("data", repo_name, "embeddings.npy"), embeddings)
                    print(f"Embeddings saved to {os.path.join('data', repo_name, 'embeddings.npy')}")
                    print(f"Embeddings shape: {embeddings.shape}")
        except Exception as e:
            print(f"Failed to generate embeddings: {e}")