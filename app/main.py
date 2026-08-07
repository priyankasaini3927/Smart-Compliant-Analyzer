from fastapi import FastAPI
from pydantic import BaseModel
import uuid
from scipy import stats
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from app.model import Complaint as ComplaintModel
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
def analyze(complaint: Complaint, db: Session = Depends(get_db)):

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

    if any(word in text for word in [ "urgent",
        "danger",
        "fire",
        "accident",
        "pothole",
        "crack",
        "collapse",
        "injury",
        "electric shock",
        "gas leak",
        "flood",
        "broken bridge",
        "damage"]):
        urgency = "High"
    else:
        urgency = "Low"

    complaint_id = uuid.uuid4().hex[:8]
    new_complaint = ComplaintModel(
        complaint_id=complaint_id,
        complaint=complaint.text,
        category=category,
        urgency=urgency,
        status="Pending",
        confidence=confidence
    )

    db.add(new_complaint)
    db.commit()
    db.refresh(new_complaint)

    return {
        "complaint_id": new_complaint.complaint_id,
        "complaint": new_complaint.complaint,
        "category": new_complaint.category,
        "urgency": new_complaint.urgency,
        "confidence": f"{new_complaint.confidence}%"
    }

@app.get("/complaints")
def get_complaints(db: Session = Depends(get_db)):

    complaints = db.query(ComplaintModel).all()

    return complaints 

@app.get("/complaints/{complaint_id}")
def get_complaint(complaint_id: str, db: Session = Depends(get_db)):

    complaint = db.query(ComplaintModel).filter(ComplaintModel.complaint_id == complaint_id).first()

    if complaint is None:
        return {
            "message": "Complaint not found"
        }

    return complaint

@app.put("/complaints/{complaint_id}")
def update_status(
    complaint_id: str,
    status_update: StatusUpdate,
    db: Session = Depends(get_db)
):

    result = db.query(ComplaintModel).filter(ComplaintModel.complaint_id == complaint_id).update({
        ComplaintModel.status: status_update.status
    })
    db.commit() 

    if result == 0:

        return {
            "message": "Complaint not found"
        }

    return {
        "message": "Status updated successfully",
        "complaint_id": complaint_id,
        "new_status": status_update.status
    }
    
@app.get("/complaints/status/{status}")
def get_complaints_by_status(status: str, db: Session = Depends(get_db)):

    complaints = db.query(ComplaintModel).filter(ComplaintModel.status == status).all() 

    return complaints

@app.get("/high-priority")
def get_high_priority_complaints(db: Session = Depends(get_db)):

    complaints = list(
        db.query(ComplaintModel).filter(ComplaintModel.urgency == "High").all()
    )

    return complaints

@app.get("/stats")
def get_stats(db: Session = Depends(get_db)):
     
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

    stats["Total"] = db.query(ComplaintModel).count()
    
    for stat in status:
        stats[stat] = db.query(ComplaintModel).filter(ComplaintModel.status == stat).count()
        
    for category in categories:
        stats[category] = db.query(ComplaintModel).filter(ComplaintModel.category == category).count()

    return stats