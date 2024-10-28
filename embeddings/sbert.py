from sentence_transformers import SentenceTransformer

# Load SBERT model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def get_sbert_text_embedding(text):
    """
    Generate embedding for a given text using SBERT model.
    """
    embedding = model.encode(text, convert_to_tensor=True)
    return embedding.cpu().numpy()
