# Hemingway-LLM

An open-source alternative to Hemingway Editor Plus with custom LLM API key support.

## Features
- Prose style analysis (readability, adverbs, passive voice).
- LLM-powered suggestions (compatible with any OpenAI-compatible API).
- CLI-only (no web interface).

## Installation
```bash
pip install textstat requests
```

## Usage
```bash
python hemingway.py --text "Your text here" --api-key YOUR_LLM_API_KEY
```

## License
MIT