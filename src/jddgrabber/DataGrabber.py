class DataGrabber:
    def __init__(self, params):
        self.params = params


    @staticmethod
    def get_grabber(grabber_classname, params):
        import jddgrabber
        cls = getattr(jddgrabber, grabber_classname)
        return cls(params)


    def fetch_data(self):
        print("This method will fetch the data from the remote server.")
