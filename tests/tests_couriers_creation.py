from endpoints.add_courier_post import Courier
from helpers.login_generator import GenLoginPassFirstName


class TestAddCourier:
    def test_courier_created_by_correct_data(self):
        gen_courier_data = GenLoginPassFirstName()
        courier = Courier(gen_courier_data.get_true_dict())
        courier.creation_request()
        courier.check_creation_status_code(201)
