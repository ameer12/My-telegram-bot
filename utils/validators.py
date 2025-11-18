import re

def is_valid_url(url: str) -> bool:
    """
    Checks if the input string is a valid URL.
    """
    regex = re.compile(
        r'^(https?://)?'                     # http:// or https:// (optional)
        r'([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})'  # domain
        r'(:\d+)?'                           # optional port
        r'(\/\S*)?$'                         # optional path
    )
    return bool(regex.match(url.strip()))
