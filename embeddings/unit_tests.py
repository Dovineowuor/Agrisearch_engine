# embeddings/unit_tests.py

import unittest
import numpy as np
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from embeddings import sbert, vggish, clip  # import relevant modules

class EmbeddingTests(unittest.TestCase):
    def test_sbert_embedding(self):
        text = "Sample agricultural query."
        embedding = sbert.get_embedding(text)
        self.assertEqual(len(embedding), 768)  # assuming 768-dim output for sbert
        self.assertIsInstance(embedding, np.ndarray)

    def test_vggish_embedding(self):
        audio_path = "tests/sample_audio.wav"
        embedding = vggish.get_embedding(audio_path)
        self.assertEqual(len(embedding), 128)  # assuming 128-dim output for vggish
        self.assertIsInstance(embedding, np.ndarray)

    def test_clip_embedding(self):
        image_path = "tests/sample_image.jpg"
        embedding = clip.get_embedding(image_path)
        self.assertEqual(len(embedding), 512)  # assuming 512-dim output for clip
        self.assertIsInstance(embedding, np.ndarray)

if __name__ == "__main__":
    unittest.main()