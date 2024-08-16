from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
import os
from dotenv import load_dotenv

import app

load_dotenv()

client = AsyncIOMotorClient(os.getenv("MONGO_DETAILS"))

def connect_to_mongo():
    global client
    client = AsyncIOMotorClient(os.getenv("MONGO_DETAILS"))
    app.database = client["Movie_list_APi"]
    print("Connected to MongoDB")

def close_mongo_connection():
    if client:
        client.close()
        print("MongoDB connection closed")

db = client.Movie_list_API

user_collection = db.get_collection("users")
movie_collection = db.get_collection("movies")
rating_collection = db.get_collection("ratings")
comment_collection = db.get_collection("comments")

print(client)
# MONGO_DETAILS = "mongodb://localhost:27017"
# MONGODB_DATABASE = os.getenv("MONGODB_DATABASE")