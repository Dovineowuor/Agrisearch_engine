# process_text_query.py

import re
import sys
import os
from nltk.tokenize import word_tokenize
# Add the project directory to sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Ensure 'punkt' tokenizer data is downloaded
from punk_downloader import ensure_punkt_downloaded
ensure_punkt_downloaded()
from punk_downloader import ensure_punkt_downloaded
ensure_punkt_downloaded()

def clean_text(text: str) -> str:
    """Cleans the input text by removing special characters and excess whitespace."""
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace
    return text

def tokenize_text(text: str) -> list:
    """Tokenizes the cleaned text into words."""
    cleaned_text = clean_text(text)
    tokens = word_tokenize(cleaned_text)
    return tokens

def analyze_query(query: str) -> dict:
    """Analyzes the text query, cleaning and tokenizing it, and queries ChromaDB."""
    cleaned_query = clean_text(query)
    tokens = tokenize_text(cleaned_query)
    token_count = len(tokens)
    from chromadb_client import client
    # Query ChromaDB for additional information
    if client:
        chroma_result = client.query(text=cleaned_query)  # Assuming ChromaDB client has a `query` method
    else:
        chroma_result = "ChromaDB client not initialized."

    return {
        'original': query,
        'cleaned': cleaned_query,
        'tokens': tokens,
        'token_count': token_count,
        'chroma_result': chroma_result
    }