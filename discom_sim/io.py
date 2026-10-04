"""Load the sourced data files that ship with the repository."""
from io import StringIO
from pathlib import Path

import pandas as pd


def read_csv(name, text=None):
    """Read data/<name>, or parse `text` if given (used by the in-browser build,
    where files and __file__ do not exist)."""
    if text is not None:
        return pd.read_csv(StringIO(text))
    data_dir = Path(__file__).resolve().parent.parent / "data"
    return pd.read_csv(data_dir / name)
