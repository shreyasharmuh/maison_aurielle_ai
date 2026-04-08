import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    timeout=30.0
)

import json
import time

def get_ai_response(query):
    system_prompt = """
You are Maison Aurielle luxury fashion AI.

Return ONLY valid JSON in this format:

{
  "title": "Outfit Name",
  "items": {
    "top": "",
    "bottom": "",
    "shoes": "",
    "accessory": ""
  },
  "style_note": ""
}

Rules:
- Minimal luxury aesthetic
- Inspired by Calvin Klein, Acne Studios, Maison Margiela
- No extra text outside JSON
"""

    for attempt in range(2):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": query}
                ],
                max_tokens=250
            )

            raw = response.choices[0].message.content.strip()

            return json.loads(raw)

        except Exception as e:
            print("AI ERROR:", e)
            time.sleep(1)

    return {
        "title": "Unavailable",
        "items": {
            "top": "-",
            "bottom": "-",
            "shoes": "-",
            "accessory": "-"
        },
        "style_note": "AI temporarily unavailable"
    }