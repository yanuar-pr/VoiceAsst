# Voice Assistant API Project

This project is part of my personal portfolio to demonstrate how a modular voice assistant system can be built using modern AI tools and clean API design.
The system is designed with a microservice structure — each service can run independently and handle its own responsibility.

## 🎯 Overview

The Voice Assistant API allows users to speak commands that are automatically transcribed and converted into structured actions.
For example:
- "home" → `{ "command_type": "navigate", "value": "home" }`
- "name yanuar email yanuar at gmail dot com" → `{ "command_type": "fill_form", "value": { ... } }`

## 🧩 Current Services

| Service                     | Description                                                                                               | Folder                   |
| --------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------ |
| **Transcriber Services**    | Converts voice or audio files into text using OpenAI Whisper (or Faster-Whisper).                         | `/TranscriberServices`   |
| **Command Parser Services** | Converts plain text (from the transcriber) into structured JSON commands via AI model (Cohere or Ollama). | `/CommandParserServices` |

Each service is self-contained, using its own FastAPI app, models, and utilities.
Both can be tested independently in local environments.

## ⚙️ Tech Stack

- Language: Python 3.10+
- Framework: FastAPI
- AI Models: Whisper (for speech-to-text), Cohere (for text understanding)
- Architecture: Modular microservices
- Documentation: OpenAPI (auto-generated via FastAPI /docs endpoint)

## 🧠 Project Flow

1. Transcriber → Converts audio into text
1. Command Parser → Converts that text into structured JSON commands
1. Future Integration (planned) → UI Agent or Frontend app executes those commands

## 🧾 License

This project is shared publicly for learning and portfolio purposes.
Free to explore, fork, or use as a reference with proper attribution.
