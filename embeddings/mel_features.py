import numpy as np
import librosa

def extract_mel_features(audio_path, sr=16000, n_mels=64, n_fft=2048, hop_length=512):
    """
    Extract mel spectrogram features from an audio file.

    Args:
        audio_path (str): Path to the audio file.
        sr (int): Sample rate for the audio file (default is 16000).
        n_mels (int): Number of mel bands to generate (default is 64).
        n_fft (int): Length of the FFT window (default is 2048).
        hop_length (int): Number of samples between each frame (default is 512).

    Returns:
        np.ndarray: Mel spectrogram features of shape (n_mels, n_frames).
    """
    # Load the audio file
    y, _ = librosa.load(audio_path, sr=sr)

    # Compute the mel spectrogram
    mel_spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels, n_fft=n_fft, hop_length=hop_length)

    # Convert to log scale (log-mel spectrogram)
    log_mel_spectrogram = librosa.power_to_db(mel_spectrogram, ref=np.max)

    return log_mel_spectrogram

def preprocess_audio_waveform(audio_waveform, sr=16000):
    """
    Preprocess audio waveform for VGGish model input.

    Args:
        audio_waveform (np.ndarray): The audio waveform.
        sr (int): Sample rate for the audio file (default is 16000).

    Returns:
        np.ndarray: Preprocessed audio waveform.
    """
    # Resample audio to 16 kHz if necessary
    if len(audio_waveform) > 0 and sr != 16000:
        audio_waveform = librosa.resample(audio_waveform, sr, 16000)
    
    # Normalize audio waveform
    audio_waveform = audio_waveform / np.max(np.abs(audio_waveform))
    
    return audio_waveform

# Additional helper functions can be added here as needed.
