# transcriber.py

from fastapi import UploadFile
import tempfile
from faster_whisper import WhisperModel

# Load the model once at module level for efficiency

# Must have compatible NVIDIA GPU or proper CUDA/cuDNN installed
model = WhisperModel("base", compute_type="float32")

# Force use of CPU by setting compute_type to "int8" and device to "cpu"
# model = WhisperModel("base", device="cpu", compute_type="int8")

async def transcribe_audio(file: UploadFile):
  # Save uploaded file to a temp file
  with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
    content = await file.read()
    temp_file.write(content)
    temp_file_path = temp_file.name

  # Transcribe audio
  segments, _ = model.transcribe(temp_file_path)

  # Combine all segments into a single string
  result_text = " ".join([segment.text for segment in segments])
  return result_text
