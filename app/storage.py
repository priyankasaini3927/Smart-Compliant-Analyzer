import pandas as pd
import uuid
from datetime import datetime

FILE_PATH = "data/complaints.csv"

def save_complaint(text, category, urgency):

    complaint_id = str(uuid.uuid4())[:8]

    new_row = {
        "id": complaint_id,
        "complaint": text,
        "category": category,
        "urgency": urgency,
        "timestamp": datetime.now()
    }

    try:
        df = pd.read_csv("data/complaints.csv")
    except:
        df = pd.DataFrame(
            columns=[
                "id",
                "complaint",
                "category",
                "urgency",
                "timestamp"
            ]
        )

    df.loc[len(df)] = new_row

    df.to_csv(FILE_PATH, index=False)

    return complaint_id