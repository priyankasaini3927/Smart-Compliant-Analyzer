from fastapi import FastAPI
from pydantic import BaseModel
import uuid
from scipy import stats
from app.database import complaints_collection
from datetime import datetime
import joblib
from typing import Literal

# Load the trained model and vectorizer
model = joblib.load("app/model.pkl")
vectorizer = joblib.load("app/vectorizer.pkl")

app = FastAPI()

class Complaint(BaseModel):
    text: str
    
class StatusUpdate(BaseModel):
    status: Literal[
        "Pending",
        "In Progress",
        "Resolved",
        "Rejected"
    ]

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/analyze")
def analyze(complaint: Complaint):

    text = complaint.text.lower()

    text_vectorized = vectorizer.transform([complaint.text])
    probabilities = model.predict_proba(text_vectorized)[0]
    print(model.classes_)
    for cls, prob in zip(model.classes_, probabilities):
        print(f"{cls}: {prob:.4f}")
    print(type(probabilities))
    confidence = max(probabilities)*100
    confidence = round(confidence, 2)
    category = model.predict(text_vectorized)[0]

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
        "created_at": datetime.now(),
        "confidence": confidence
    })

    return {
        "complaint_id": complaint_id,
        "complaint": complaint.text,
        "category": category,
        "urgency": urgency,
        "confidence": f"{confidence}%"
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

@app.put("/complaints/{complaint_id}")
def update_status(
    complaint_id: str,
    status_update: StatusUpdate
):

    result = complaints_collection.update_one(
        {"complaint_id": complaint_id},
        {
            "$set": {
                "status": status_update.status
            }
        }
    )

    if result.modified_count == 0:
        return {
            "message": "Complaint not found"
        }

    return {
        "message": "Status updated successfully",
        "complaint_id": complaint_id,
        "new_status": status_update.status
    }
    
@app.get("/complaints/status/{status}")
def get_complaints_by_status(status: str):

    complaints = list(
        complaints_collection.find(
            {"status": status},
            {"_id": 0}
        )
    )

    return complaints

@app.get("/high-priority")
def get_high_priority_complaints():

    complaints = list(
        complaints_collection.find(
            {"urgency": "High"},
            {"_id": 0}
        )
    )

    return complaints

@app.get("/stats")
def get_stats():
     
    status = [
    "Pending",
    "In Progress",
    "Resolved",
    "Rejected"
    ]
    categories = [
    "Health",
    "Safety",
    "Transport",
    "Roads",
    "Water",
    "Electricity",
    "Other"
    ]

    stats = {}

    stats["Total"] = complaints_collection.count_documents({})
    
    for stat in status:
        stats[stat] = complaints_collection.count_documents(
            {"status": stat}
        )
        
    for category in categories:
        stats[category] = complaints_collection.count_documents(
            {"category": category}
        )


    return stats