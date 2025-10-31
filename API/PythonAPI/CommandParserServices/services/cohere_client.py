import httpx
import os
from dotenv import load_dotenv
from fastapi import HTTPException
from models.cohere_message import CohereMessage

# load .env file
load_dotenv()

AI_MODEL = "command-a-03-2025"
API_URL = "https://api.cohere.ai/v2/chat"
API_KEY = os.getenv("COHERE_API_KEY")

async def call_cohere_chat(
  messages: list[CohereMessage],
  model: str = AI_MODEL,
  is_json_format: bool = True
) -> str:
  data = {
    "model": model,
    "messages": [
      {"role": m.role.value, "content": m.content}
      for m in messages
    ],
    "stream": False,
    "temperature": 0
  }

  if is_json_format:
    data["response_format"] = {"type": "json_object"}

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
  }

  try:
    timeout = httpx.Timeout(10.0, connect = 5.0)
    async with httpx.AsyncClient(timeout = timeout) as client:
      response = await client.post(
        API_URL,
        headers = headers,
        json = data
      )

      response.raise_for_status()
      result = response.json()

      # Extract response: message.content[0].text
      if (
        "message" not in result or
        "content" not in result["message"] or
        not isinstance(result["message"]["content"], list) or
        not result["message"]["content"]
      ):
        raise HTTPException(
          status_code = 500,
          detail=f"Invalid response format: {result}"
        )

      return result["message"]["content"][0]["text"].strip()

  except httpx.HTTPStatusError as e:
    raise HTTPException(
      status_code = e.response.status_code,
      detail = f"Cohere error: {e.response.text}"
    )

  except httpx.RequestError as e:
    raise HTTPException(
      status_code = 503,
      detail = f"Cohere server unreachable: {str(e)}"
    )

  except Exception as e:
    raise HTTPException(
      status_code = 500,
      detail = f"Unhandled error: {str(e)}"
    )
