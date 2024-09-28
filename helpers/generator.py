from datetime import datetime


class GenCourierData:
    def __init__(self):
        self.gen_id = datetime.now().strftime("%Y%m%d%H%M%S")
        self.login = f"lgfedqa{self.gen_id}"
        self.password = f"pssfedqa{self.gen_id}"
        self.first_name = f"frnfedqa{self.gen_id}"

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