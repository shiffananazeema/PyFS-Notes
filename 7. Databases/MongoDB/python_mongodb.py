from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create or switch to a database
db = client["test_database"]

# Create or switch to a collection (like a table)
collection = db["users"]

# Insert a document (like a row)
user = {"name": "Shiffana", "age": 25, "email": "shiff@example.com"}
collection.insert_one(user)

# Find and print all users
for u in collection.find():
    print(u)
