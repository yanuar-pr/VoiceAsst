from fastapi import FastAPI

from core.cohere_command_parser import build_cohere_prompt
# from core.ollama_command_parser import build_ollama_prompt
from models.cohere_message import CohereMessage
from models.parser_request import ParserRequest
from models.parser_response import ParserResponse
from services.cohere_client import call_cohere_chat
# from services.ollama_client import call_ollama

app = FastAPI()

@app.post("/command-parser")
async def parser(req: ParserRequest):
  # Cohere integration
  messages: list[CohereMessage] = build_cohere_prompt(req.location, req.prompt)
  raw_output: str = await call_cohere_chat(messages)

  response = ParserResponse()
  response.from_ai_response(raw_output)

  return response

  # Ollama integration temporarily disabled.
  # Model testing deferred — current responses not aligned with required JSON schema for CommandParser.
  # TODO: Revisit when local model configuration is stable.
  # prompt: str = build_ollama_prompt(req.location, req.prompt)
  # return await call_ollama(prompt)
