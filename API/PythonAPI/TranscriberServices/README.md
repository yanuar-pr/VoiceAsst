# Transcriber Services – Voice Assistant Project

A simple FastAPI microservice that converts voice or audio files into text using OpenAI's Whisper model.  
Useful for voice assistants, subtitles, speech notes, and more.

For example, you can upload an audio file (recorded using a microphone), and this service will return the spoken words as text.

## Example Use Case

For example, you can upload an audio file (recorded using microphone), and this service will return the spoken words as text.

Example: ```"welcome to voice assistant"```

## 📦 Prerequisites

- Python 3.10.11
  - [Download Python 3.10.11 from official site](https://www.python.org/downloads/release/python-31011/)
- Git
- VS Code (recommended) with the following extensions:
  - Python by Microsoft
  - Pylance (optional, for IntelliSense)
  - Debugger for Python (`debugpy`)
- NVIDIA GPU (optional): If you have a compatible CUDA GPU, `faster-whisper` will automatically use it for faster transcription.
  - Tested with PyTorch 2.2.2 + cu121


## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
cd VoiceAsst/API/PythonAPI/TranscriberServices
```

### 2. Create a virtual environment

Windows:
```bash
python -m venv .venv
.venv\Scripts\Activate
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Check GPU support (optional)

You can check if GPU is available for inference before running the API:
```bash
python services/verify_gpu.py
```

If output is `cuda`, GPU acceleration is active.
If `cpu`, it will run slower but still functional.

Activate the code in `\services\transcriber.py` based on gpu or cpu:
```bash
# gpu enabled
model = WhisperModel("base", compute_type="float32")

# use cpu, gpu disabled
model = WhisperModel("base", device="cpu", compute_type="int8")
```


## 🛠️ Update Setup Instructions

(Optional) Update `requirements.txt` to reflect all installed packages:
```bash
pip freeze > requirements.txt
```
