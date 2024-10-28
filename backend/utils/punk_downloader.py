import nltk
import logging
import os

# Configure logging to include the file name and line number
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)'
)
logger = logging.getLogger(__name__)

def ensure_punkt_downloaded():
    search_paths = [
        '/home/dov3/nltk_data',
        '/home/dov3/Work/AgriSearch_AI_search_engine/.venv/nltk_data',
        '/home/dov3/Work/AgriSearch_AI_search_engine/.venv/share/nltk_data',
        '/home/dov3/Work/AgriSearch_AI_search_engine/.venv/lib/nltk_data',
        '/usr/share/nltk_data',
        '/usr/local/share/nltk_data',
        '/usr/lib/nltk_data',
        '/usr/local/lib/nltk_data'
    ]

    for path in search_paths:
        try:
            # Check if the 'punkt' tokenizer data is available in the current path
            nltk.data.find('tokenizers/punkt', paths=[path])
            logger.info(f"Punkt tokenizer data found in {path}.")
            return path
        except LookupError:
            continue

    # If not found in any of the paths, download the 'punkt' tokenizer data
    download_dir = os.path.expanduser('~/nltk_data')
    logger.info("Punkt tokenizer data not found. Downloading now...")
    nltk.download('punkt', download_dir=download_dir)
    logger.info(f"Punkt tokenizer data downloaded successfully to {download_dir}.")
    return download_dir

# Ensure that the 'punkt' tokenizer data is downloaded
punkt_data_path = ensure_punkt_downloaded()
nltk.data.path.append(punkt_data_path)
logger.info(f"Punkt tokenizer data is available in {punkt_data_path}.")
