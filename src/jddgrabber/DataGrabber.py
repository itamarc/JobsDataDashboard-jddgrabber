class DataGrabber:
    """
    Superclass to grabber classes and also implements the factory.
    """
    def __init__(self, params):
        self.params = params


    @staticmethod
    def get_grabber(grabber_classname, params):
        import jddgrabber
        cls = getattr(jddgrabber, grabber_classname)
        return cls(params)


    def fetch_data(self):
        """
        This method must be implemented in subclasses.
        """
        raise NotImplementedError
