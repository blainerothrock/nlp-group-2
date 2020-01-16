import requests


class WikiParser():

    def __init__(self):
        self.S = requests.Session()
        self.URL = "https://en.wikipedia.org/w/api.php"

    def fetch_page(self, title):
        params = {
            "action": "parse",
            "page": title,
            "format": "json"
        }

        res = self.S.get(
            url=self.URL,
            params=params
        )

        data = res.json()
        return data
