from enum import Enum

class CohereRoleType(str, Enum):
  system = "system"
  user = "user"
  assistant = "assistant"
