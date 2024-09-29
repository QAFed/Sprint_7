import requests
from main_data import Links


class GetOrdersList:
    def __init__(self, limit=None):
        self.endpoint = "/api/v1/orders"
        self.response = None
        self.limit = None
        if limit:
            self.limit = f'?{limit}'

    def request(self):
        self.response = requests.get(Links.MAIN_URL+self.endpoint+self.limit)

    def check_status_code(self, status_code):
        assert self.response.status_code == status_code
