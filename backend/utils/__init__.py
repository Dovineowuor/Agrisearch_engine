import os
import time
import pickle
from werkzeug.utils import secure_filename

# In-memory cache dictionary
cache = {}

class CacheEntry:
    """Class to represent a cache entry with an expiration time."""
    def __init__(self, value, expiry_time):
        self.value = value
        self.expiry_time = expiry_time

def save_file(file, upload_folder):
    """Saves the uploaded file to the specified upload folder and returns the file path."""
    # Ensure the upload folder exists
    os.makedirs(upload_folder, exist_ok=True)
    
    # Secure the filename and construct the full file path
    filename = secure_filename(file.filename)
    file_path = os.path.join(upload_folder, filename)
    
    # Save the file
    file.save(file_path)
    return file_path

CACHE_DIR = 'cache/dir'

def cache_results(key, value, expiration_seconds=None):
    """Caches the results both in memory and on disk using pickle, with optional expiration."""
    # Cache in memory
    expiry_time = time.time() + expiration_seconds if expiration_seconds else None
    cache[key] = CacheEntry(value, expiry_time)

    # Cache on disk
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)
    
    cache_path = os.path.join(CACHE_DIR, f"{key}.pkl")
    with open(cache_path, 'wb') as cache_file:
        pickle.dump((value, expiry_time), cache_file)

def fetch_from_cache(key):
    """Fetches results from cache if available and not expired; returns None if not found or expired."""
    # First check in-memory cache
    entry = cache.get(key)
    if entry:
        if entry.expiry_time is None or time.time() < entry.expiry_time:
            return entry.value
        else:
            # Entry has expired, remove it from memory cache
            del cache[key]

    # Check on disk cache if not found in memory
    cache_path = os.path.join(CACHE_DIR, f"{key}.pkl")
    if os.path.exists(cache_path):
        with open(cache_path, 'rb') as cache_file:
            value, expiry_time = pickle.load(cache_file)
            if expiry_time is None or time.time() < expiry_time:
                # Cache is valid; return the value
                cache[key] = CacheEntry(value, expiry_time)  # Update in-memory cache
                return value
            else:
                # Disk cache entry has expired
                os.remove(cache_path)  # Remove the expired cache file
    return None

def clear_cache(key):
    """Clears a specific key from the in-memory and disk cache."""
    if key in cache:
        del cache[key]
    
    cache_path = os.path.join(CACHE_DIR, f"{key}.pkl")
    if os.path.exists(cache_path):
        os.remove(cache_path)

def clear_all_cache():
    """Clears all cached results in memory and on disk."""
    cache.clear()
    
    if os.path.exists(CACHE_DIR):
        for filename in os.listdir(CACHE_DIR):
            file_path = os.path.join(CACHE_DIR, filename)
            os.remove(file_path)

def clean_cache():
    """Removes expired entries from the in-memory cache."""
    keys_to_remove = [key for key, entry in cache.items() if entry.expiry_time and time.time() >= entry.expiry_time]
    for key in keys_to_remove:
        del cache[key]
