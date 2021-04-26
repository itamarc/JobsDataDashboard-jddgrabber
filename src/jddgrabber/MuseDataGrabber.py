from jddgrabber.DataGrabber import DataGrabber


class MuseDataGrabber(DataGrabber):
    def fetch_data(self):
        print("This method will fetch the data from the Muse REST service.")
        print("params: ", self.params)
        return {}
