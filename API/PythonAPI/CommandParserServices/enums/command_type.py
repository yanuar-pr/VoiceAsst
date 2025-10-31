from enum import Enum

class CommandType(str, Enum):
  NAVIGATE = "navigate"
  FILL_FORM = "fill_form"
  NONE = "none"
