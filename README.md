# AgriSearch AI Search Engine
AgriSearch AI is an advanced search engine designed specifically for agricultural data. It leverages AI to provide accurate and relevant search results.

### Overview

This project is a **vector search application** built using **ChromaDB** as the backend database. It allows users to input queries such as text, images, videos, and other media formats, and retrieves results that are most similar based on vector embeddings. The project is designed to support multiple embedding models like CLIP, SBERT, Whisper, and VGGish, and uses these models to encode data into vectors, enabling semantic similarity search.

This application specifically targets the **agriculture** domain, helping users search through a dataset of agricultural resources (e.g., images of crops, farming equipment, videos on techniques, or articles). It provides farmers, researchers, and businesses with a powerful tool to find relevant information using advanced AI-based vector search.

### Features

- **Multimedia Search**: Supports text, image, video, and audio search.
- **Vector Embedding Models**:
  - [CLIP](https://github.com/openai/CLIP): For processing both text and image embeddings.
  - [SBERT](https://www.sbert.net/): For semantic text embedding.
  - [Whisper](https://github.com/openai/whisper): For video/audio transcription.
  - [VGGish](https://github.com/tensorflow/models/tree/master/research/audioset/vggish): For audio embedding.
- **ChromaDB Integration**: Utilizes ChromaDB for efficient vector search and similarity matching.
- **Bootstrap Frontend**: A clean, responsive UI built with **Bootstrap**, featuring search functionalities and media displays.
- **Flask Backend**: Backend API developed using **Flask**, handling file uploads, embeddings, and ChromaDB interactions.
- **Extensible**: Designed to easily add support for additional data types and embedding models.
  
### Project Architecture

```plaintext
├── backend/
│   ├── app.py               # Flask app entry point
│   ├── models.py            # Define ChromaDB models and schema
│   ├── embeddings.py        # Embedding model (CLIP, SBERT, Whisper, etc.) handling
│   ├── chromadb_client.py   # Integration with ChromaDB
│   └── utils.py             # Helper functions (file uploads, conversions, etc.)
│
├── frontend/
│   ├── static/              # CSS, JS, images
│   │   ├── css/
│   │   │   └── style.css    # Custom styles for Bootstrap
│   │   └── js/
│   │       └── script.js    # Optional JavaScript for interaction
│   ├── templates/           # HTML files for rendering
│   │   └── index.html       # Main frontend page with Bootstrap
│   └── app.js               # Frontend interaction logic, AJAX calls, etc.
│
├── embeddings/
│   ├── clip.py              # CLIP model handling (text & image embeddings)
│   ├── sbert.py             # SBERT for text embeddings
│   ├── whisper.py           # Whisper for video/audio transcription
│   └── vggish.py            # VGGish for audio embeddings
│
├── data/
│   ├── uploads/             # Directory to store uploaded images, videos, etc.
│   └── dataset/             # Optional initial dataset
│
├── config.py                # Configuration for the project (API keys, paths, etc.)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

### Getting Started

This section guides you through setting up and running the application locally.

#### Prerequisites

1. **Python 3.8+**: Make sure you have Python installed. You can download it from [here](https://www.python.org/downloads/).
2. **pip**: Install Python dependencies using `pip` (comes bundled with Python).
3. **ChromaDB**: You'll need to install and configure **ChromaDB** for vector storage.

#### Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/vector-search-app.git
   cd vector-search-app
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   Make sure to install the required Python libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Modify `config.py` to set up your API keys, ChromaDB connection details, and any other configurations.

5. **Initialize ChromaDB**:
   Make sure ChromaDB is running and configured to accept your embeddings. Refer to the [ChromaDB documentation](https://chromadb.com/docs) for setup instructions.

6. **Run the Flask app**:
   Start the backend Flask server:
   ```bash
   python backend/app.py
   ```

7. **Access the front-end**:
   Open a browser and navigate to `http://localhost:5000`. The main interface should be available with search options for images, text, and more.

#### Project Configuration

The project configuration can be customized by editing `config.py`. You'll need to provide:

- **API keys** (for using pre-trained models like CLIP, SBERT, Whisper, etc.).
- **ChromaDB settings** for vector storage and search.

### Usage

After setting up the project, you can:

1. **Upload Data**: Upload text, images, or video/audio files to the app via the frontend.
2. **Generate Embeddings**: The backend will automatically process the media and generate vector embeddings using the chosen AI models (CLIP, SBERT, Whisper, etc.).
3. **Perform Search**: Input a query (text or media), and the app will search through the dataset for similar items based on vector similarity.
4. **View Results**: The frontend will display the closest matches, including media previews or text snippets.

### Available Models

This project utilizes several AI models to process and generate embeddings for different types of content:

- **CLIP**: For text and image embedding.
- **SBERT**: For semantic text embedding.
- **Whisper**: For audio/video transcription and embedding.
- **VGGish**: For audio embedding and matching.

Each model is designed to handle a specific type of media, allowing for versatile search across multimedia content.

### Extending the Project

The project is designed to be flexible and extensible. You can:

- **Add new embedding models**: Simply create new scripts in the `embeddings/` directory and integrate them into the pipeline.
- **Support new media types**: Extend the front-end and backend to handle additional types of content.
- **Enhance the search interface**: Add filters, advanced search options, or more sophisticated ranking algorithms.

### Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request once your changes are ready for review.

Please make sure to follow the [Contributor's Guide](CONTRIBUTING.md) (if applicable).

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- **ChromaDB** for their powerful vector search capabilities.
- **OpenAI's CLIP** for image and text embeddings.
- **Hugging Face** for their SBERT implementation.
- **OpenAI Whisper** for video and audio transcription.

---
