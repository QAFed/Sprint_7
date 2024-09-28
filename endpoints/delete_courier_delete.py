import requests
from main_data import Links


class CourierDelete:
    def __init__(self):
        self.endpoint = "/api/v1/courier/"
        self.response = None

    def delete_request(self, id):
        self.response = requests.delete(Links.MAIN_URL+self.endpoint+f'{id}')

    def check_status_code(self, status_code):
        assert self.response.status_code == status_code