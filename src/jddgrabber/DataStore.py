import pymongo
from pymongo import MongoClient
from jddgrabber import JDDConfig as cnf
import json
import os

# This config will be received, not read here again
config = cnf.load_config(r'config.yaml')

cluster = MongoClient(config["mongdb"]["connection"])
db = cluster["jobsdatadb"]
collection = db["jobsdata"]

#collection.delete_one({"_id": 1})

#results = collection.find({"name": { "$regex": ".*Engineer.*" }})
#for result in results:
#    print(result["name"])


config_dir = os.path.join(os.getcwd(), "conf")
with open(os.path.join(config_dir, r'sampledatamuse.json')) as file:
    data = json.load(file)

collection.insert_many(data)


