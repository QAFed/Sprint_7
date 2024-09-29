import requests
from main_data import Links


class OrderAccept:
    def __init__(self, courier_id, order_id):
        self.endpoint = "/api/v1/orders/accept/"
        self.courier_id = str(courier_id)
        self.order_id = ""
        if order_id:
            self.order_id = str(order_id)+"?"
        self.response = None

    def request(self):
        self.response = requests.put(Links.MAIN_URL+self.endpoint+self.order_id+'courierId='+self.courier_id)

    def check_status_code(self, status_code):
        assert self.response.status_code == status_code

    def check_response_json(self, expect_dict):
        assert self.response.json() == expect_dict
