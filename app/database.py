from pymongo import MongoClient
import certifi

MONGO_URI = "MY_MONGODM_URI"

client = MongoClient(
    MONGO_URI,
    tlsCAFile=certifi.where()
)

db = client["smart_complaint_db"]

complaints_collection = db["complaints"]
