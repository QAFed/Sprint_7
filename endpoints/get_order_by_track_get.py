import requests
from main_data import Links


class GetOrder:
    def __init__(self, track):
        self.endpoint = "/api/v1/orders/track"
        self.track = track
        self.response = None

    def request(self):
        self.response = requests.get(Links.MAIN_URL+self.endpoint+f'?t={self.track}')

    def check_status_code(self, status_code):
        assert self.response.status_code == status_code

    def check_response_json(self, expect_dict):
        assert self.response.json() == expect_dict
