import os
import sys
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add the project directory to sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Ensure 'punkt' tokenizer data is downloaded
from utils.punk_downloader import ensure_punkt_downloaded
ensure_punkt_downloaded()

from utils.process_text_query import analyze_query
from utils.process_audio_query import analyze_audio_query
from utils.secure_filename import secure_filename

app = Flask(__name__)

# Configure Flask app
app.config.update(
    CELERY_BROKER_URL=os.getenv('CELERY_BROKER_URL', 'amqp://explorer:pa55word@localhost:5672//'),
    CELERY_RESULT_BACKEND='rpc://'
)

# Import and initialize Celery after Flask app is created
from celery_app import create_celery
celery = create_celery(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query/text', methods=['POST'])
def query_text():
    """Endpoint to handle text queries."""
    data = request.json
    text = data.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Process the text query
    results = analyze_query(text)
    return jsonify({'results': results}), 200

@app.route('/query/audio', methods=['POST'])
def query_audio():
    """Endpoint to handle audio file uploads and processing."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the uploaded audio file securely
    audio_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
    file.save(audio_path)

    # Process the audio query
    results = analyze_audio_query(audio_path)
    return jsonify({'results': results}), 200

@app.route('/test/analyze_query', methods=['GET'])
def test_analyze_query():
    """Endpoint to test the analyze_query function with sample data."""
    sample_text = "This is a sample text to test the analyze_query function."
    results = analyze_query(sample_text)
    return jsonify({'results': results}), 200

if __name__ == '__main__':
    app.run(debug=True)