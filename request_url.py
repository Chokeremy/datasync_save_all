import requests


class RequestUrl:

    def __init__(self, url, headers, json):
        self.response = requests.post(url, headers=headers, json=json)

    def parse_url(self):
        return self.response.content.decode()
