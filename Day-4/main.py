import pdfplumber
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def get_data():
    with pdfplumber.open("invoice.pdf") as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text()
    return full_text