import logging
from jddgrabber.DataStore import DataStore


class DataGrabber:
    """
    Superclass to grabber classes and also implements the factory.
    """

    def __init__(self, params):
        self.params = params
        self.logger = logging.getLogger('jddgrabberlog')

    @staticmethod
    def get_grabber(grabber_classname, params):
        """
        Grabber factory method.
        """
        import jddgrabber
        cls = getattr(jddgrabber, grabber_classname)
        return cls(params)

    def fetch_data(self):
        """
        This method must be implemented in subclasses.

        It should grab the data from the remote API, handling paging if needed,
        and then save the data in the database using the 'save_data' function.
        """
        raise NotImplementedError

    def save_data(self, data):
        """
        Save some grabbed data in the database.
        """
        ds = DataStore(self.params)
        ds.insert_data(data)
