import requests
from main_data import Links


class CourierSignUp:
    def __init__(self, payload):
        self.endpoint = "/api/v1/courier"
        self.payload = payload
        self.response = None

    def sign_up_request(self):
        self.response = requests.post(Links.MAIN_URL+self.endpoint, json=self.payload)

    def check_creation_status_code(self, payload):
        assert self.response.status_code == payload
