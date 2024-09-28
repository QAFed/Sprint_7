from datetime import datetime


class GenLoginPassFirstName:
    def __init__(self):
        self.gen_id = datetime.now().strftime("%Y%m%d%H%M%S")
        self.login = f"lgfedqa{self.gen_id}"
        self.password = f"pssfedqa{self.gen_id}"
        self.first_name = f"frnfedqa{self.gen_id}"

    def get_true_dict(self):
        return {
            "login": self.login,
            "password": self.password,
            "firstName": self.first_name
        }