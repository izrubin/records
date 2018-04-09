#!/usr/bin/env python

"""
Package to obtain occurrence records from GBIF for a given taxon in a range of
years
"""


import requests
import pandas as pd


class Records:
    """
    Create an instance of the class Records for occurrence records from GBIF,
    for a user-entered range of years and taxon. Results are stored in a panda
    # DataFrame.
    """
    def __init__(self, q=None, interval=None):

        # base search API URL
        self.baseurl = "http://api.gbif.org/v1/occurrence/search?"

        # set parameters for the search with default API options plus
        # user-entered taxon and range of years
        self.params = {
            "q": q,
            "year": ",".join([str(i) for i in interval]),
            "basisOfRecord": "PRESERVED_SPECIMEN",
            "hasCoordinate": "true",
            "hasGeospatialIssue": "false",
            "country": "US",
            "offset": "0",
            "limit": "300"
        }

        # repeat query until all records are obtained and store in pd DataFrame
        self.df = pd.DataFrame(self._get_all_records())

    # to make one large dictionary with all of the results by appending ea addl
    # 300 records
    def _get_all_records(self):
        "repeat search until all records are obtained"
        data = []

        while 1:  # while true
            # make request and store results
            res = requests.get(
                url=self.baseurl,
                params=self.params,
            )

            # this would return an error message if it didn't work (else None)
            res.raise_for_status()

            # increment counter; convert string to an integer and then add 300
            self.params["offset"] = str(int(self.params["offset"]) + 300)

            # concatenate data
            idata = res.json()
            # pull out just the results and append to the data dictionary
            data += idata["results"]

            # stop at the end of the records
            if idata["endOfRecords"]:
                break

        return data
