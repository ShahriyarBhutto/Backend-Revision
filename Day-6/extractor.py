from dotenv import load_dotenv
from openai import OpenAI
import os, json
import pdfplumber

load_dotenv()

client = OpenAI(
    base_url = "",
    api_key = os.environ[""]
)


def extract_data_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text
    return text

