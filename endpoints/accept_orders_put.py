import requests
from main_data import Links


class OrderAccept:
    def __init__(self, courier_id, order_id):
        self.endpoint = "/api/v1/orders/accept/"
        self.courier_id = courier_id
        self.order_id = order_id
        self.response = None

    def request(self):
        self.response = requests.put(Links.MAIN_URL+self.endpoint+f'{self.order_id}?courierId={self.courier_id}')

    def check_status_code(self, status_code):
        assert self.response.status_code == status_code