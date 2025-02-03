# faiss_index.py
import faiss
import numpy as np
import os

def create_index(embeddings):
    """
    Create a FAISS index for the embeddings.
    """
    if embeddings.ndim == 1:
        embeddings = embeddings.reshape(1, -1)  # Reshape to 2D if necessary
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

if __name__ == "__main__":
    repo_name = "digital_slide_archive"  # Example repo
    embeddings_file = os.path.join("data", repo_name, "embeddings.npy")
    
    if not os.path.exists(embeddings_file):
        print(f"Error: {embeddings_file} does not exist. Run embed_text.py first.")
    else:
        try:
            embeddings = np.load(embeddings_file)
            if embeddings.size == 0:
                print("Error: Embeddings file is empty.")
            else:
                print(f"Loaded embeddings with shape: {embeddings.shape}")
                index = create_index(embeddings)
                faiss.write_index(index, os.path.join("data", repo_name, "index.faiss"))
                print(f"FAISS index saved to {os.path.join('data', repo_name, 'index.faiss')}")
        except Exception as e:
            print(f"Failed to create FAISS index: {e}")