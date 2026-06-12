from pymongo import MongoClient
import certifi

MONGO_URI = "mongodb+srv://sainipriyanka3927_db_user:BQFyOJBtg4DoTzK7@complaintanalyzer.aeihmbu.mongodb.net/?appName=complaintanalyzer"

client = MongoClient(
    MONGO_URI,
    tlsCAFile=certifi.where()
)

db = client["smart_complaint_db"]

complaints_collection = db["complaints"]
