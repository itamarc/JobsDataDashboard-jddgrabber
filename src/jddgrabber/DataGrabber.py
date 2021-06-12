import logging
from jddgrabber.DataStore import DataStore


class DataGrabber:
    """
    Superclass to grabber classes and also implements the factory.
    """
    datastore = None

    def __init__(self, params, config):
        self.params = params
        self.config = config
        self.logger = logging.getLogger('jddgrabberlog')
        self.logger.debug("DataGrabber init: '" + params['name'] +
            "' using class: " + params['class_name'])

    @staticmethod
    def get_grabber(grabber_classname, params, config):
        """
        Grabber factory method.
        """
        import jddgrabber
        cls = getattr(jddgrabber, grabber_classname)
        return cls(params, config)

    def fetch_data_page(self, page):
        """
        This method must be implemented in subclasses.

        It should grab the data from the remote API for a single page.

        This method must return a tuple: (nextpage, data)
        nextpage - the next page number or -1 if there is no more pages to get.
        data - the data grabbed.
        """
        raise NotImplementedError

    def fetch_data(self):
        """
        This method must be implemented in subclasses.

        It should grab the data from the remote API, handling paging if needed,
        and then save the data in the database using the 'save_data' function.
        """
        page = 0
        next = 0
        while (next >= 0):
            page = next
            (next, data) = self.fetch_data_page(page)
            if not data is None:
                self.put_jdd_run_id(data)
                self.save_data(data)
            else:
                self.logger.warning("Empty response received on page "+str(page))
        self.logger.info(self.params['name']+" - pages grabbed: "+str(page))

    def put_jdd_run_id(self, data):
        for d in data:
            d['jdd_run_id'] = self.config['jdd_run_id']

    def save_data(self, data):
        """
        Save some grabbed data in the database.
        """
        if DataGrabber.datastore is None:
            DataGrabber.datastore = DataStore(self.config)
        DataGrabber.datastore.save_data(data)
