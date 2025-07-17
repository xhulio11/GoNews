from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from colorama import Fore, Style
import hashlib
import json 


class mongodb():


    def __init__(self, host_ip, port, database, collection):

        self.MONGO_HOST = host_ip
        self.MONGO_PORT = port
        self.DATABASE_NAME = database
        self.COLLELCTION_NAME = collection
        
        # Establish Connection 
        # Connect to MongoDB
        try:
            self.client = MongoClient(self.MONGO_HOST, self.MONGO_PORT)
            print("Connected to MongoDB successfully!")
        except Exception as e:
            print(f"Failed to connect to MongoDB: {e}")
            exit()


    # This function is used to make a unique id
    # content is a dict object 
    def generate_hash(self, content):
        """Generate a stable SHA256 hash for structured data like dict or list."""
        json_str = json.dumps(content, sort_keys=True)
        return hashlib.sha256(json_str.encode('utf-8')).hexdigest()
    
    def insert_articles(self, articles):
        
        documents = [None for _ in articles]
        
        for i, topic in enumerate(articles):
            # creating hash codes for every collection of articles 
            temp_hash = self.generate_hash(topic)

            document = {
                "_id": temp_hash, 
                "articles":topic, 
                "processed":False
            }
            documents[i] = document

        # Bulk insert
        try:
            # Select the database and collection
            db = self.client[self.DATABASE_NAME]
            collection = db[self.COLLELCTION_NAME]
            # Insert the Documents
            collection.insert_many(documents, ordered=False)
        
        except Exception as e:
            print("Insertion warning:", e)
