from fastapi import FastAPI
from pydantic import BaseModel
import uuid
from app.database import complaints_collection
from datetime import datetime

app = FastAPI()

class Complaint(BaseModel):
    text: str
        
@app.get("/")
def home():
    return {"status": "running"}

@app.post("/analyze")
def analyze(complaint: Complaint):

    text = complaint.text.lower()

    if any(word in text for word in ["road", "pothole", "street"]):
        category = "Roads"

    elif any(word in text for word in ["water", "pipe", "leakage"]):
        category = "Water"

    elif any(word in text for word in ["electricity", "power", "light"]):
        category = "Electricity"

    else:
        category = "Other"

    if any(word in text for word in ["urgent", "danger", "fire", "accident"]):
        urgency = "High"
    else:
        urgency = "Low"

    complaint_id = str(uuid.uuid4())[:8]

    complaints_collection.insert_one({
        "complaint_id": complaint_id,
        "complaint": complaint.text,
        "category": category,
        "urgency": urgency,
        "status": "Pending",
        "created_at": datetime.now()
    })

    return {
        "complaint_id": complaint_id,
        "complaint": complaint.text,
        "category": category,
        "urgency": urgency
    }
    
@app.get("/complaints")
def get_complaints():

    complaints = list(
        complaints_collection.find(
            {},
            {"_id": 0}
        )
    )

    return complaints

@app.get("/stats")
def get_stats():

    total = complaints_collection.count_documents({})

    roads = complaints_collection.count_documents(
        {"category": "Roads"}
    )

    water = complaints_collection.count_documents(
        {"category": "Water"}
    )

    electricity = complaints_collection.count_documents(
        {"category": "Electricity"}
    )

    return {
        "total": total,
        "roads": roads,
        "water": water,
        "electricity": electricity
    }