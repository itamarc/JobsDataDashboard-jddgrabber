from jddgrabber.DataGrabber import DataGrabber

class MuseDataGrabber(DataGrabber):
    """
    DataGrabber subclass that implements the fetch_data getting data from The Muse REST service.

    The service is available at:
    https://www.themuse.com/api/public/jobs
    """
    def fetch_data(self):
        print("This method will fetch the data from the Muse REST service.")
        print("params: ", self.params)
        return {}
