from fastapi import FastAPI
from pydantic import BaseModel
import uuid
from scipy import stats
from app.database import complaints_collection
from datetime import datetime
import joblib

# Load the trained model and vectorizer
model = joblib.load("app/model.pkl")
vectorizer = joblib.load("app/vectorizer.pkl")

app = FastAPI()

class Complaint(BaseModel):
    text: str
        
@app.get("/")
def home():
    return {"status": "running"}

@app.post("/analyze")
def analyze(complaint: Complaint):

    text = complaint.text.lower()

    text_vectorized = vectorizer.transform([complaint.text])
    probabilities = model.predict_proba(text_vectorized)[0]
    confidence = max(probabilities)*100
    confidence = round(confidence, 2)
    print(probabilities)
    print(type(probabilities))
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
        "confidence": confidence
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

    for category in categories:
        stats[category] = complaints_collection.count_documents(
            {"category": category}
        )

    stats["Total"] = complaints_collection.count_documents({})

    return stats