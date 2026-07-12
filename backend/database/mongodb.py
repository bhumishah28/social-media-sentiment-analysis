import os

from dotenv import load_dotenv
from pymongo import MongoClient


# -------------------------
# Load Environment Variables
# -------------------------

load_dotenv()


# -------------------------
# Read Configuration
# -------------------------

MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")


# -------------------------
# MongoDB Client
# -------------------------

client = MongoClient(MONGODB_URI)


# -------------------------
# Database
# -------------------------

database = client[DATABASE_NAME]


# -------------------------
# Collection
# -------------------------

predictions_collection = database[COLLECTION_NAME]