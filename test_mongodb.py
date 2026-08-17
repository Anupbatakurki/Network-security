import os
import certifi
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_DB_URL = os.getenv("MONGODB_URL_KEY")

if not MONGO_DB_URL:
    raise ValueError("MONGODB_URL_KEY not found in .env")

print("Connecting to MongoDB Atlas...")

try:
    client = MongoClient(
        MONGO_DB_URL,
        tlsCAFile=certifi.where(),
        serverSelectionTimeoutMS=10000
    )

    client.admin.command("ping")

    
    print("MongoDB Atlas connection SUCCESS!")
   

except Exception as e:
    print("MongoDB connection FAILED:")
    print(e)