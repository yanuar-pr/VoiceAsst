from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from services.transcriber import transcribe_audio

app = FastAPI()

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
  text = await transcribe_audio(file)
  return JSONResponse({"text": text})
