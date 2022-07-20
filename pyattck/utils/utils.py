import os
from pathlib import Path
from urllib.parse import urlparse


def get_absolute_path(path: str):
    if path.startswith("http") or path.startswith("https"):
        return path
    else:
        try:
            if Path(path):
                return os.path.abspath(os.path.expanduser(os.path.expandvars(path)))
        except Exception as e:
            pass


def is_path(value: str) -> bool:
    try:
        Path(value)
        return True
    except Exception as e:
        pass
    return False


def is_web_url(value: str) -> bool:
    """Return True if this is a valid HTTP or HTTPS URL."""
    try:
        return urlparse(value).scheme in ["http", "https"]
    except Exception as e:
        pass
    return False
