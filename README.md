# AI Task 3 - Voice Chatbot

> A simple Python voice chatbot that converts speech into text using Whisper, generates responses with Cohere, and converts the responses back into speech using gTTS.

---

## Overview

This project demonstrates a complete voice interaction pipeline by combining:

- **Speech-to-Text** using OpenAI Whisper
- **Large Language Model** responses using Cohere
- **Text-to-Speech** using Google Text-to-Speech (gTTS)

The chatbot plays a recorded voice message, transcribes it into text, generates an AI response, then converts that response into speech.

🎥 [AI Voice Chatbot Demo](https://drive.google.com/file/d/1cwLHMiKMFqYY43BrItic3WMhgrh809FG/view?usp=drivesdk)

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Speech-to-Text | OpenAI Whisper (`small.en`) |
| LLM | Cohere API |
| Text-to-Speech | gTTS |
| Audio Playback | playsound |
| Audio Processing | FFmpeg |
| Language | Python 3.10 |

---

## Project Setup

The following tools and packages were used during development:

```bash
conda create -n voicebot python=3.10
conda activate voicebot
winget install ffmpeg
pip install -U openai-whisper cohere gTTS playsound
```

---

## API Configuration

The Cohere API key is loaded from an environment variable rather than being stored inside the source code.

Example:
```bash
set COHERE_API_KEY=your_api_key_here
```

---

## Running the Project

```bash
python voicebot.py
```

The program processes the recorded audio, transcribes it using Whisper, generates a response with Cohere, converts the response to speech using gTTS, and plays the generated audio.

---

## Notes

- Uses the English-only Whisper `small.en` model.
- Requires an active Cohere API key to generate responses.
