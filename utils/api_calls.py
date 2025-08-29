import requests
from config.config import config

def call_openai_api(prompt):
    url = "https://api.openai.com/v1/completions"
    headers = {
        "Authorization": f"Bearer {config.OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "prompt": prompt,
        "max_tokens": 4096  # 300
    }
    response = requests.post(url, headers=headers, json=data)

    # Log the response for debugging
    print("Response Status Code:", response.status_code)
    print("Response JSON:", response.json())

    return response.json()