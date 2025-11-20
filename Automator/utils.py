import os
from pathlib import Path

def ensure_dir(dirpath):
    Path(dirpath).mkdir(parents=True, exist_ok=True)
