import re

def secure_filename(filename):
    """Return a secure version of the filename."""
    # Use a regex to replace unwanted characters with underscores
    filename = re.sub(r'[^A-Za-z0-9_.-]', '_', filename)

    # Remove leading and trailing underscores
    filename = filename.strip('_')

    # Ensure filename is not empty
    if not filename:
        return 'default_filename.txt'  # Default filename if all characters are stripped

    # Return the secure filename
    return filename
