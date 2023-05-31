from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import json
import os


# Load environment variables from .env
load_dotenv("./dotenv/")
#Connect to the data base
Client = MongoClient(os.getenv("ENTRYPOINT"), connect=False)
