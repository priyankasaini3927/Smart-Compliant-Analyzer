from sqlalchemy import Column, String, Enum, DECIMAL, TIMESTAMP
from app.database import Base

class Complaint(Base):
    __tablename__ = "complaints"

    complaint_id = Column(String(8), primary_key=True)

    complaint = Column(String(250), nullable=False)

    category = Column(
        Enum(
            "Health",
            "Safety",
            "Transport",
            "Roads",
            "Water",
            "Electricity",
            "Other"
        ),
        nullable=False
    )

    urgency = Column(
        Enum("High", "Low"),
        nullable=False
    )

    confidence = Column(DECIMAL(5,2))

    status = Column(
        Enum(
            "Pending",
            "In Progress",
            "Resolved",
            "Rejected"
        ),
        default="Pending"
    )

    created_at = Column(TIMESTAMP)

    updated_at = Column(TIMESTAMP)