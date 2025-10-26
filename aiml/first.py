import requests
import json
from datetime import datetime
import time

API_KEY = "AIzaSyAJjx7NXszJSZ4H2Vm6KmmwMaEPXZmdJ4w"
API_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={"AIzaSyAJjx7NXszJSZ4H2Vm6KmmwMaEPXZmdJ4w"}"
INPUT_FILE = "text.txt"
OUTPUT_FILE = "llm_responses.json"

def read_prompts(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

def ask_llm(prompt):
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()

    data = response.json()
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        return json.dumps(data, indent=2)

def save_to_json(responses, output_path):
    data = {
        "created_at": datetime.now().isoformat(),
        "responses": responses
    }
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    print("starting gemini api interaction...")
    prompts = read_prompts(INPUT_FILE)
    if not prompts:
        print("No prompts found in the file.")
        return

    results = []
    for i, prompt in enumerate(prompts, start=1):
        print(f"\nPrompt {i}/{len(prompts)}: {prompt}")
        try:
            reply = ask_llm(prompt)
            print("Response received.")
            results.append({"prompt": prompt, "response": reply})
        except Exception as e:
            print(f"Error: {e}")
            results.append({"prompt": prompt, "error": str(e)})
        time.sleep(1)

    save_to_json(results, OUTPUT_FILE)
    print(f"\nDone. Responses saved to '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    main()
