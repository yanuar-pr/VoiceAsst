from pydantic import BaseModel
from enums.cohere_role_type import CohereRoleType

class CohereMessage(BaseModel):
  role: CohereRoleType
  content: str
