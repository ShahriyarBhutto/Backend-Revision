import pdfplumber
from openai import OpenAI
from dotenv import load_dotenv
import json , os


load_dotenv()

client = OpenAI(
    base_url = "",
    api_key = os.environ[""]
)

def extract_text_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in file.pages:
            text += page.extract_text()
    return text

def get_structured_data(text):
    prompt = f"""
    Extract order_id, customer, amount, date from this invoice.
    Return ONLY valid JSON, no markdown.
    Text: {text}
    """
    response = client.chat.completion.create(
        model = "",
        messages = [{"role":"user","content":prompt}]
    )

    clean_text = response.choice[0].message.content.strip().replace("```json","").replace("```","")
    return json.loads(clean_text)