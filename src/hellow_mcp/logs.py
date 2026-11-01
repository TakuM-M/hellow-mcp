from collections import deque
from pathlib import Path

import yaml

# uv --directory sets the working directory to the project root.
CONFIG_PATH = Path("config.yaml")


def read_logs(path: str, lines: int = 100) -> list[str]:
    """Return the last lines of a log file on the allowlist in config.yaml."""
    allowed = yaml.safe_load(CONFIG_PATH.read_text())["allowed_log_files"]
    if path not in allowed:
        raise ValueError(f"{path} is not allowed. Allowed files: {allowed}")
    with open(path, errors="replace") as file:
        return [line.rstrip("\n") for line in deque(file, maxlen=lines)]
