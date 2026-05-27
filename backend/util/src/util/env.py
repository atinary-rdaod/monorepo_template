import os


def require_env(key: str) -> str:
    value = os.environ.get(key)
    if value is None or value == "":
        msg = f"Missing required environment variable: {key}"
        raise RuntimeError(msg)
    return value
