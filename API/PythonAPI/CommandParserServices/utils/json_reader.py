import json
from pathlib import Path
from typing import Union

def read_json_as_dict(path: Union[str, Path]) -> dict:
  """Read a JSON file and return as Python dict."""
  with open(path, encoding = "utf-8") as f:
    return json.load(f)

def read_json_as_str(path: Union[str, Path], compact: bool = False) -> str:
  """Read a JSON file and return as JSON-formatted string."""
  with open(path, encoding = "utf-8") as f:
    content : str = f.read().strip()

    if compact:
      return content.replace("\n", "").replace("  ", "")

    return content
