import textstat
import requests
import argparse
import json


def analyze_text(text):
    """Analyze prose style using textstat."""
    return {
        "readability": textstat.flesch_reading_ease(text),
        "adverbs": textstat.adverb_count(text),
        "passive_voice": textstat.passive_voice_count(text),
    }


def get_llm_suggestions(text, api_key, api_url="https://api.openai.com/v1/chat/completions"):
    """Fetch LLM-powered suggestions."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "system", "content": "You are a writing assistant. Suggest improvements for clarity, conciseness, and style."}, {"role": "user", "content": text}],
    }
    response = requests.post(api_url, json=data, headers=headers)
    return response.json()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hemingway-LLM: Open-source prose analysis with LLM suggestions.")
    parser.add_argument("--text", type=str, required=True, help="Text to analyze")
    parser.add_argument("--api-key", type=str, required=True, help="LLM API key")
    parser.add_argument("--api-url", type=str, default="https://api.openai.com/v1/chat/completions", help="LLM API URL (OpenAI-compatible)")
    args = parser.parse_args()
    
    analysis = analyze_text(args.text)
    print("Analysis:")
    print(json.dumps(analysis, indent=2))
    
    suggestions = get_llm_suggestions(args.text, args.api_key, args.api_url)
    print("\nSuggestions:")
    print(json.dumps(suggestions, indent=2))