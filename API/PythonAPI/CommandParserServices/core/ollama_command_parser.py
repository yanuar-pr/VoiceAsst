import yaml
from pathlib import Path

from rag.docs_loader import load_menu_mapping, load_fill_form_mapping
from utils.json_reader import read_json_as_str

ASSETS_DIR = Path(__file__).resolve().parent / "assets" / "ollama_command_parser"

JSON_FORMAT_FILE = "json_format.json"
JSON_GUIDELINE_FILE = "json_guideline.yaml"
PROMPT_FILE = "prompt.yaml"

def build_ollama_prompt(user_location: str, user_prompt: str) -> str:
  menu_content: str = load_menu_mapping()
  fill_form_content: dict = load_fill_form_mapping()
  json_command_format = load_json_format()
  has_form = user_location in fill_form_content
  json_guideline: str = load_json_guideline(has_form)

  prompt: str = load_prompt(has_form)

  return prompt.format(
    user_prompt = user_prompt,
    menu_content = menu_content,
    fill_form_content = fill_form_content,
    json_command_format = json_command_format,
    json_guideline = json_guideline
  )

def load_json_format() -> str:
  return read_json_as_str(ASSETS_DIR / JSON_FORMAT_FILE, True)

def load_json_guideline(has_form: bool) -> str:
  with open(ASSETS_DIR / JSON_GUIDELINE_FILE, encoding="utf-8") as f:
    data = yaml.safe_load(f)

  return data["with_fill_form"] if has_form else data["without_fill_form"]

def load_prompt(has_form: bool) -> str:
  with open(ASSETS_DIR / PROMPT_FILE, encoding="utf-8") as f:
    data = yaml.safe_load(f)

  return data["with_field_form"] if has_form else data["without_field_form"]
