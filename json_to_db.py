import json
from pymongo import MongoClient, ASCENDING, DESCENDING
from dotenv import load_dotenv
import os

load_dotenv()

mongodb_uri = os.getenv("MONGODB_URI")

client = MongoClient(mongodb_uri)
db = client.kimo_courses

# Drop existing collection if any
db.courses.drop()

# Create indices for efficient retrieval
db.courses.create_index([("name", ASCENDING)])
db.courses.create_index([("date", DESCENDING)])
db.courses.create_index([("ratings.average", DESCENDING)])

# Load courses from the JSON file
with open('courses.json', 'r') as file:
    courses = json.load(file)
    for course in courses:
        course['ratings'] = {'positive': 0, 'negative': 0, 'average': 0.0}
    db.courses.insert_many(courses)

print("Courses have been successfully imported into MongoDB.")
