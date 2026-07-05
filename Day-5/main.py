from fastapi import FastAPI,UploadFile, HTTPException
from extractor import extract_text_pdf, get_structured_data
import json

app = FastAPI

@app.post("/post")
async def extract_invoice(file: UploadFile):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400,detail="Please uplaod a pdf file")
    
    text = extract_text_pdf(file.file)
    try:
        data = get_structured_data(text)
        return data
    except json.JSONDecodeError:
        raise HTTPException(status_code=500,detail="LLM is valid, but unable to find the data")