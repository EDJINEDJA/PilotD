from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import json
import os
import time


# Load environment variables from .env
load_dotenv("./dotenv/")
#Connect to the data base

def connect_with_retry(connection_string, max_retries=5, initial_delay=1):
    retries = 0
    delay = initial_delay

    while retries < max_retries:
        try:
            client = MongoClient(connection_string, serverSelectionTimeoutMS=60000,server_api=ServerApi('1'))
            # Test the connection by running a sample query
            client.admin.command('ismaster')
            print("Successfully connected to MongoDB.")
            return client
        except Exception as e:
            print(f"Connection attempt failed: {str(e)}")
            retries += 1
            time.sleep(delay)
            delay *= 2

    raise Exception("Unable to connect to MongoDB after multiple retries.")

# Usage:
Client = connect_with_retry(os.getenv("ENTRYPOINT"))

#Client = MongoClient(os.getenv("ENTRYPOINT"), server_api=ServerApi('1'))
