from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
import cv2
import numpy as np
import easyocr
import spacy
import re
import dateparser
from io import BytesIO
from model_loader import load_yolo_model, safe_yolo_predict

app = FastAPI()


reader = easyocr.Reader(['en', 'hi'])
nlp = spacy.load("en_core_web_sm")


yolo = load_yolo_model("yolov8n.pt")

def is_pii(text: str):
    reasons = []

    
    if re.search(r'\b\d{4}\s\d{4}\s\d{4}\b', text) or re.search(r'\b\d{12}\b', text):
        reasons.append("Aadhaar number")
    
    
    if re.search(r'\b[A-Z]{5}[0-9]{4}[A-Z]\b', text):
        reasons.append("PAN number")

    
    if re.search(r'\b[6-9]\d{9}\b', text):
        reasons.append("Phone number")

    
    if re.search(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text):
        reasons.append("Email address")

    
    if (
        re.search(r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b', text) or 
        re.search(r'जन्म[\s]*तिथि[\s:/-]*\d{1,2}[/-]\d{1,2}[/-]\d{2,4}', text) or
        dateparser.parse(text, settings={'DATE_ORDER': 'DMY'})
    ):
        reasons.append("Date of birth or similar")

    
    if re.search(r'\b(पुरुष|महिला|अन्य)\b', text):
        reasons.append("Gender (Hindi)")

    
    if re.search(r'[अ-ह]+(?:\s[अ-ह]+)+', text):
        reasons.append("Hindi name detected")

    
    try:
        doc = nlp(text)
        for ent in doc.ents:
            if ent.label_ in ['PERSON', 'ORG', 'GPE']:
                reasons.append(f"{ent.label_} detected via NER")
    except:
        pass  

    return reasons if reasons else None


def pixelate(img, box, factor=15):
    
    x1, y1 = map(int, box[0])
    x2, y2 = map(int, box[2])
    if x2 > x1 and y2 > y1:
        roi = img[y1:y2, x1:x2]
        if roi.size == 0:
            return img
        roi = cv2.resize(roi, (max(1, roi.shape[1] // factor), max(1, roi.shape[0] // factor)))
        roi = cv2.resize(roi, (x2 - x1, y2 - y1), interpolation=cv2.INTER_NEAREST)
        img[y1:y2, x1:x2] = roi
    return img

@app.post("/process")
async def process(file: UploadFile = File(...)):
    
    img_bytes = await file.read()
    img_np = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)

    
    yolo_results = safe_yolo_predict(yolo, img_np)

    
    results = reader.readtext(img_np)
    pii_log = []

    for box, text, _ in results:
        reasons = is_pii(text)
        if reasons:
            img_np = pixelate(img_np, box)
            pii_log.append({"text": text, "reason": reasons})

    
    success, encoded = cv2.imencode(".jpg", img_np)
    if not success:
        return {"error": "Failed to encode image"}

    return StreamingResponse(BytesIO(encoded.tobytes()), media_type="image/jpeg", headers={"Content-Disposition": "inline; filename=masked.jpg"})
