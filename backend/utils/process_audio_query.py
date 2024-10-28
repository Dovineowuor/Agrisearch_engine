# process_audio_query.py

import speech_recognition as sr

def recognize_audio(file_path: str) -> str:
    """Converts audio to text using the SpeechRecognition library."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)  # Read the entire audio file

    try:
        # Using Google Web Speech API for recognition
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Audio could not be understood."
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

def analyze_audio_query(file_path: str, chromadb_client=None) -> dict:
    """Analyzes the audio query, returns the recognized text, and interacts with ChromaDB."""
    recognized_text = recognize_audio(file_path)
    
    # Process text with ChromaDB if initialized
    if chromadb_client:
        chroma_result = chromadb_client.query(text=recognized_text)  # Assuming query function exists
    else:
        chroma_result = "ChromaDB client not initialized."

    return {
        'recognized_text': recognized_text,
        'chroma_result': chroma_result,
        'file_path': file_path
    }
