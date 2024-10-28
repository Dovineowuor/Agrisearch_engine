from transformers import CLIPProcessor, CLIPModel
import torch

# Load CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def get_clip_embedding(text=None, image=None):
    """
    Generate embeddings using the CLIP model for text or images.
    
    :param text: Text input to generate embedding (optional).
    :param image: Image input to generate embedding (optional).
    :return: Embeddings (tensor).
    """
    inputs = processor(text=text, images=image, return_tensors="pt", padding=True)
    with torch.no_grad():
        outputs = model.get_text_features(**inputs) if text else model.get_image_features(**inputs)
    return outputs
