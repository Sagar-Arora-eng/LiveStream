import pymongo
from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/testing"
cluster = MongoClient('MONGO_URI')
db = cluster['videostream']