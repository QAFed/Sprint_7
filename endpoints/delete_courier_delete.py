import requests
from main_data import Links


class CourierDelete:
    def __init__(self, id):
        self.endpoint = "/api/v1/courier/"
        self.response = None
        self.id = id
    def request(self):
        self.response = requests.delete(Links.MAIN_URL+self.endpoint+f'{self.id}')

    def check_status_code(self, status_code):
        assert self.response.status_code == status_code

    def check_response_json(self, expect_dict):
        assert self.response.json() == expect_dict