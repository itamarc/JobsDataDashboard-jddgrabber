class DataGrabber:
    params = {}


    def __init__(self, params):
        self.params = params


    def get_grabber(self, grabber_classname, params):
        return type(grabber_classname, (DataGrabber), params)


    def fetch_data(self):
        print("This method will fetch the data from the remote server.")
