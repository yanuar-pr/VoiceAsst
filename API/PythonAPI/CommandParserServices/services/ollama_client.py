import httpx
from fastapi import HTTPException

OLLAMA_MODEL = "llama3.2:latest"
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_JSON_FORMAT = "json"

async def call_ollama(prompt: str, is_json_format: bool = True) -> str:
  data = {
    "model": OLLAMA_MODEL,
    "prompt": prompt,
    "stream": False
  }

  if is_json_format:
    data['format'] = OLLAMA_JSON_FORMAT

  headers = {
    "Content-Type": "application/json"
  }

  try:
    timeout = httpx.Timeout(10.0, connect = 5.0)
    async with httpx.AsyncClient(timeout = timeout) as client:
      response = await client.post(
        OLLAMA_URL,
        headers = headers,
        json = data
      )

      response.raise_for_status()
      result = response.json()

      if "response" not in result:
        raise HTTPException(
          status_code = 500,
          detail = f"Invalid response format: {result}"
        )

      return result["response"].strip()

  except httpx.HTTPStatusError as e:
    raise HTTPException(
      status_code = e.response.status_code,
      detail = f"Ollama error: {e.response.text}"
    )

  except httpx.RequestError as e:
    raise HTTPException(
      status_code = 503,
      detail = f"Ollama server unreachable: {str(e)}"
    )

  except Exception as e:
    raise HTTPException(
      status_code = 500,
      detail = f"Unhandled error: {str(e)}"
    )
