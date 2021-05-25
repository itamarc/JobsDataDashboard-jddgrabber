from pymongo import MongoClient
from jddgrabber import JDDConfig as cnf
import json
import os


class DataStore:
    collection = None

    def __init__(self, params):
        self.params = params

    def get_collection(self):
        if (self.collection is None):
            cluster = MongoClient(self.params["mongdb"]["connection"])
            db = cluster["jobsdatadb"]
            self.collection = db["jobsdata"]
        return self.collection

    def save_data(self, data):
        self.get_collection().insert_many(data)

    ###########################################################################
    # The code below this point was written only for testing purposes
    ###########################################################################

    def insert_sample_data(self, collection):
        config_dir = os.path.join(os.getcwd(), "conf")
        with open(os.path.join(config_dir, r'sampledatamuse.json')) as file:
            data = json.load(file)

        self.save_data(data)

    def testing_code(self):
        # This config will be received, not read here again
        config = cnf.load_config(r'config.yaml')

        collection = self.get_collection(config)

        # collection.delete_one({"_id": 1})

        # results = collection.find({"name": { "$regex": ".*Engineer.*" }})
        # for result in results:
        #    print(result["name"])

        self.insert_sample_data(collection)
