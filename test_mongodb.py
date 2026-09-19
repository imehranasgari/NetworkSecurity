import urllib.parse
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

username = urllib.parse.quote_plus("username")
password = urllib.parse.quote_plus("password")


cluster_host = "cluster.cluster_host.mongodb.net"

uri = f"mongodb+srv://{username}:{password}@{cluster_host}/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(e)