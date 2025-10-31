# Command Parser Services – Voice Assistant Project

A simple FastAPI microservice that interprets **natural language user commands** into structured JSON commands, using **Cohere AI**.

This service is part of the **Voice Assistant Project**, which converts user voice input → text → structured command.  
It helps the system understand what the user wants to do, such as *navigate to a page* or *fill in a form field*.


## 💬 Example Use Case

Input (text): `name yanuar email yanuar at gmail dot com message sent me your price list submit`

API Response:
```json
{
  "command_type": "fill_form",
  "value": {
    "name": "yanuar",
    "email": "yanuar@gmail.com",
    "message": "sent me your price list",
    "submit": ""
  }
}
```

Input (text): `home`

API Response:
```json
{
  "command_type": "navigate",
  "value": "home"
}
```

These responses can then be used by the frontend or automation system to perform actual actions (e.g., filling a form, navigating to a page, etc.).


## 📦 Prerequisites

- Python 3.10.11
  - [Download Python 3.10.11 from official site](https://www.python.org/downloads/release/python-31011/)
- Git
- VS Code (recommended) with the following extensions:
  - Python by Microsoft
  - Pylance (optional, for IntelliSense)
  - Debugger for Python (`debugpy`)
- Cohere API Key
  - [Create a free account on Cohere](https://dashboard.cohere.com/)
  - Copy your API key from the Cohere dashboard


## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
cd VoiceAsst/API/PythonAPI/CommandParserServices
```

### 2. Create and activate a virtual environment

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

### 4. Run the API locally

```bash
uvicorn main:app --reload
```

## 🔍 Example Request

Send a `POST` request to `/command-parser`:

```bash
curl -X POST "http://127.0.0.1:8002/command-parser"   -H "Content-Type: application/json"   -H "x-api-key: YOUR_API_KEY"   -d "{\"location\": \"contact\",\"prompt\": \"home\"}"
```

Response example:
```json
{
  "command_type": "navigate",
  "value": "home"
}
```

## 🛠️ Update Setup Instructions

(Optional) Update `requirements.txt` to reflect all installed packages:
```bash
pip freeze > requirements.txt
```
