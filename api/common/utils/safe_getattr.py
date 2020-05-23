from typing import Any

def safe_getattr(obj: Any, attr: str, default: Any = None):
    try:
        return getattr(obj, attr, default)
    except (AttributeError):
        return None
