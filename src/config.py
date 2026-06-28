"""Configuration module."""

DEFAULT_CONFIG = {
    "app_name": "gh-test-playground",
    "version": "1.0.0",
    "debug": True,
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30,
    "features": {
        "auth": True,
        "cache": True,
        "metrics": False,
    }
}

def get_config(key: str, default=None):
    return DEFAULT_CONFIG.get(key, default)
