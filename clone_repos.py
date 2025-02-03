# clone_repos.py
from git import Repo
import os

def clone_repo(repo_url, output_dir):
    """
    Clone a GitHub repository into the specified directory.
    Skip cloning if the directory already exists.
    """
    try:
        if os.path.exists(output_dir):
            print(f"Directory {output_dir} already exists. Skipping clone.")
            return
        os.makedirs(output_dir)
        Repo.clone_from(repo_url, output_dir)
        print(f"Cloned {repo_url} into {output_dir}")
    except Exception as e:
        print(f"Failed to clone {repo_url}: {e}")

def extract_text_from_repo(repo_dir):
    """
    Extract text from markdown and text files in a repository.
    """
    text_data = ""
    try:
        for root, _, files in os.walk(repo_dir):
            for file in files:
                if file.endswith(".md") or file.endswith(".txt"):
                    with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                        text_data += f.read() + "\n"
    except Exception as e:
        print(f"Failed to extract text from {repo_dir}: {e}")
    return text_data

if __name__ == "__main__":
    repos = [
        "https://github.com/digitalslidearchive/digital_slide_archive",
        "https://github.com/DigitalSlideArchive/digitalslidearchive.info"
    ]
    for repo_url in repos:
        repo_name = repo_url.split("/")[-1]
        repo_dir = os.path.join("data", repo_name)
        
        # Clone the repository
        clone_repo(repo_url, repo_dir)
        
        # Extract text from the repository
        text_data = extract_text_from_repo(repo_dir)
        
        # Save the extracted text to a file
        if text_data:
            with open(os.path.join(repo_dir, "extracted_text.txt"), "w", encoding="utf-8") as f:
                f.write(text_data)
            print(f"Extracted text saved to {os.path.join(repo_dir, 'extracted_text.txt')}")
        else:
            print(f"No text extracted from {repo_dir}")