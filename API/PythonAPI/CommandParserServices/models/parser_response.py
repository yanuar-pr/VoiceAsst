import json
from pydantic import BaseModel
from typing import Union

from enums.command_type import CommandType

class ParserResponse(BaseModel):
  command_type: str = CommandType.NONE
  value: Union[str, dict[str, str]] = ""

  def from_ai_response(self, raw_output: str):
    try:
      parsed = json.loads(raw_output)

      # update existing instance fields safely
      self.command_type = parsed.get("command_type", self.command_type)
      self.value = parsed.get("value", self.value)

    except Exception:
      # silently ignore invalid AI response
      pass
