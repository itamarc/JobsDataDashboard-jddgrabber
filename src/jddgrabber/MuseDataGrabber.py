from jddgrabber.DataGrabber import DataGrabber
import requests  # type: ignore


class MuseDataGrabber(DataGrabber):
    """
    DataGrabber subclass that implements the fetch_data getting data from
    The Muse REST service.

    The service is available at:
    https://www.themuse.com/api/public/jobs
    """

    def fetch_data_page(self, page):
        """
        Grab the data from the remote API for a single page.

        This method must return the next page number or -1 if there is no more
        pages to get.
        """
        self.logger.debug(
            "On MuseDataGrabber fetch_data_page (page: " + str(page) + ")")
        queryurl = self.build_request_url(page)
        self.logger.debug("queryurl: "+queryurl)
        response = requests.get(queryurl)
        data = None
        next = -1
        if response.status_code == 200:
            respjson = response.json()
            totpages = respjson['page_count']
            data = respjson['results']
            if totpages > page:
                next = page + 1
            self.logger.debug("Page "+str(page)+" of " +
                              str(totpages)+" (next: "+str(next)+")")
        else:
            # This means something went wrong.
            self.logger.error("Error grabbing The Muse data: " +
                              str(response.status_code)+": "+response.json()['error'])
            # better stop here
            next = -1
            # TODO: check if those headers are there and log them if they are
            # X-RateLimit-Remaining: How many requests you can still make at this time
            # X-RateLimit-Limit: The total number of requests you're allowed to make
            # X-RateLimit-Reset: Seconds remaining before the rate limit resets
            # self.logger.debug("X-RateLimit-Remaining: " + str(response.headers['X-RateLimit-Remaining']) + " X-RateLimit-Limit: " + str(
            #     response.headers['X-RateLimit-Limit']) + " X-RateLimit-Reset: " + str(response.headers['X-RateLimit-Reset']))
            # from json.encoder import JSONEncoder
            # self.logger.debug("Response Headers: " + JSONEncoder().encode(str(response.headers)))
            # print("Response Headers: " + str(response.headers))

        return (next, data)

    def build_request_url(self, page):
        fullurl = self.params['url'] + "?api_key=" + \
            self.params['api_key'] + "&page=" + str(page)
        for cat in self.params['category']:
            fullurl += "&category=" + cat
        for level in self.params['level']:
            fullurl += "&level=" + level
        for loc in self.params['location']:
            fullurl += "&location=" + loc
        return fullurl
