import whisper
from embeddings.sbert import get_sbert_embedding

# Load Whisper model (you can adjust model size: 'tiny', 'base', 'small', 'medium', 'large')
model = whisper.load_model("base")

def transcribe_audio(audio_path):
    """
    Transcribe an audio or video file to text using Whisper.
    
    :param audio_path: Path to the audio or video file.
    :return: Transcribed text.
    """
    result = model.transcribe(audio_path)
    return result['text']

def get_whisper_audio_embedding(audio_path):
    """
    Generate transcription and embedding for an audio or video file using Whisper and SBERT.
    
    :param audio_path: Path to the audio or video file.
    :return: Embedding (numpy array).
    """
    # First, transcribe the audio using Whisper
    transcription = transcribe_audio(audio_path)
    
    # Then, generate an embedding for the transcription using SBERT
    return get_sbert_embedding(transcription)
