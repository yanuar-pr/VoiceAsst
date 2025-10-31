from pathlib import Path

from utils.json_reader import read_json_as_dict, read_json_as_str

DOCS_FOLDER = Path(__file__).resolve().parent.parent / "docs"

FILL_FORM_FILE = "fill_form.json"
FORM_FILE = "form.json"
MENU_FILE = "menu.json"

def load_menu_mapping() -> str:
  return read_json_as_str(DOCS_FOLDER / MENU_FILE, True)

def load_fill_form_mapping() -> dict:
  return read_json_as_dict(DOCS_FOLDER / FILL_FORM_FILE)

def load_form_mapping() -> dict:
  return read_json_as_dict(DOCS_FOLDER / FORM_FILE)

def load_fields_mapping(form_name: str) -> list:
  data = load_form_mapping()
  return data.get(form_name, {}).get("fields", [])

def load_guidelines_mapping(form_name: str) -> dict:
  data = load_form_mapping()
  return data.get(form_name, {}).get("guidelines", {})
