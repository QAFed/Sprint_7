from datetime import datetime


class GenCourierData:
    def __init__(self):
        self.gen_id = datetime.now().strftime("%Y%m%d%H%M%S")
        self.login = f"lgfedqa{self.gen_id}"
        self.password = f"pssfedqa{self.gen_id}"
        self.first_name = f"frnfedqa{self.gen_id}"
        self.sidn_in_id = None
    def get_data_for_sign_up_courier(self):
        return {
            "login": self.login,
            "password": self.password,
            "firstName": self.first_name
        }

    def get_data_for_sign_in_courier(self):
        return {
            "login": self.login,
            "password": self.password
        }

class GenOrderData:

    def get_data_for_order(self):
        return {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                "BLACK"
            ]
        }