import yaml
from pathlib import Path
from models.cohere_message import CohereMessage, CohereRoleType
from rag.docs_loader import (
  load_menu_mapping,
  load_form_mapping,
  load_fields_mapping,
  load_guidelines_mapping
)
from utils.json_reader import read_json_as_str

ASSETS_DIR = Path(__file__).resolve().parent / "assets" / "cohere_command_parser"

JSON_FORMAT_FILE = "json_format.json"
JSON_GUIDELINE_FILE = "json_guideline.yaml"
PROMPT_FILE = "prompt.yaml"

def build_cohere_prompt(
  user_location: str,
  user_prompt: str
) -> list[CohereMessage]:
  # load static content
  menu_content: str = load_menu_mapping()
  form_content: dict = load_form_mapping()
  fields_content: dict = load_fields_mapping(user_location)
  guidelines_content: dict = load_guidelines_mapping(user_location)
  has_form = user_location in form_content
  json_command_format = load_json_format()
  json_guideline: str = load_json_guideline(has_form)

  # load templates
  system_prompt_template, user_prompt_template = load_prompt(has_form)

  # fill placeholders
  system_prompt_filled = system_prompt_template.format(
    menu_content = menu_content,
    fields_content = fields_content if has_form else "",
    guidelines_content = guidelines_content,
    json_command_format = json_command_format,
    json_guideline = json_guideline
  )

  user_prompt_filled = user_prompt_template.format(
    user_prompt = user_prompt
  )

  # build messages
  messages: list[CohereMessage] = []

  # each non-empty line in sys_prompt → system role
  for line in system_prompt_filled.splitlines():
    if line.strip():
      messages.append(
        CohereMessage(role = CohereRoleType.system, content = line.strip())
      )

  # user part → single user role
  messages.append(
    CohereMessage(role = CohereRoleType.user, content = user_prompt_filled.strip())
  )

  return messages

def load_json_format() -> str:
  return read_json_as_str(ASSETS_DIR / JSON_FORMAT_FILE, True)

def load_json_guideline(has_form: bool) -> str:
  with open(ASSETS_DIR / JSON_GUIDELINE_FILE, encoding="utf-8") as f:
    data = yaml.safe_load(f)

  return data["with_fill_form"] if has_form else data["without_fill_form"]

def load_prompt(has_form: bool) -> tuple[str, str]:
  with open(ASSETS_DIR / PROMPT_FILE, encoding="utf-8") as f:
    data = yaml.safe_load(f)

  system_prompt = data["with_field_form"] if has_form else data["without_field_form"]
  user_prompt = data["user_prompt"]

  return system_prompt, user_prompt
