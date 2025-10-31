from pydantic import BaseModel

class ParserRequest(BaseModel):
  location: str
  prompt: str
