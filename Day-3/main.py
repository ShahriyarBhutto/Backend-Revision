import os
from openai import OpenAI
from dotenv import load_dotenv
from fastapi import FastAPI
import json

load_dotenv()

app = FastAPI()

prompt = """
Extract name and age from this text. 
Return ONLY valid JSON, no other text, no markdown formatting.
Format: {"name": "...", "age": ...}

Text: Ali, 25 saal
"""



client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)

@app.get("/test")
def test():
     response = client.chat.completions.create(
            # model="openrouter/auto",
            model = "poolside/laguna-xs-2.1:free"
            messages=[{"role": "user", "content": prompt}]
        )
     text = response.choices[0].message.content.strip()
     if text.startswith("```"):
        text = text.split("```")[1].replace("json","").strip()
     try:
       data = json.loads(text)
       return data
     except json.JSONDecodeError:
        print("LLM ne valid JSON nahi diya, dobara try karo")