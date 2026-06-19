from pymongo import MongoClient
import certifi

MONGO_URI = "MY_MONGODB_URI"

client = MongoClient(
    MONGO_URI,
    tlsCAFile=certifi.where()
)

print(client.server_info())

print("Connected Successfully")
