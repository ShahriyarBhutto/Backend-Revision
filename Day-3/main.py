import os
from openai import OpenAI
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)

@app.get("/test")
def test():
    try:
        response = client.chat.completions.create(
            model="openrouter/auto",
            messages=[{"role": "user", "content": "Explain APIs in 2 lines"}]
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}