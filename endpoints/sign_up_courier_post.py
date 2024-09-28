import requests
from main_data import Links


class CourierSignUp:
    def __init__(self, payload):
        self.endpoint = "/api/v1/courier"
        self.payload = payload
        self.response = None

    def request(self):
        self.response = requests.post(Links.MAIN_URL+self.endpoint, json=self.payload)

    def check_status_code(self, status_code):
        assert self.response.status_code == status_code
