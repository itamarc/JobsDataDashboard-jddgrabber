import logging
from pymongo import MongoClient


class DataStore:
    collection = None

    def __init__(self, params):
        self.params = params
        self.logger = logging.getLogger('jddgrabberlog')
        self.logger.debug("DataStore init.")

    def get_collection(self):
        if (DataStore.collection is None):
            cluster = MongoClient(self.params["mongodb"]["connection"])
            db = cluster["jobsdatadb"]
            DataStore.collection = db["jobsdata"]
        return DataStore.collection

    def save_data(self, data):
        try:
            self.logger.debug("DataStore - saving data - # records: " + str(len(data)))
            self.get_collection().insert_many(data)
        except Exception:
            self.logger.exception("DataStore - error saving data: " + str(data))
