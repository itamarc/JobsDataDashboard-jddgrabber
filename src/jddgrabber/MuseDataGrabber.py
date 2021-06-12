from jddgrabber.DataGrabber import DataGrabber


class MuseDataGrabber(DataGrabber):
    """
    DataGrabber subclass that implements the fetch_data getting data from The Muse REST service.

    The service is available at:
    https://www.themuse.com/api/public/jobs
    """

    def fetch_data_page(self, page):
        """
        Grab the data from the remote API for a single page.

        This method must return the next page number or -1 if there is no more
        pages to get.
        """
        self.logger.debug("On MuseDataGrabber fetch_data_page (page: " + str(page) + ")")
        print("TODO: This method will fetch the data from the Muse REST service.")
        print("params: ", self.params)
        next = -1 # for now grab the first page and stop
        return (next, [{"name": "test themuse"}])
