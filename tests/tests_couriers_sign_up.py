from endpoints.sign_up_courier_post import CourierSignUp
from helpers.generator import GenCourierData


class TestAddCourier:
    def test_courier_created_by_correct_data(self):
        gen_courier_data = GenCourierData()
        courier_sign_up = CourierSignUp(gen_courier_data.get_data_for_sign_up_courier())
        courier_sign_up.sign_up_request()
        courier_sign_up.check_status_code(201)
        print(courier_sign_up.payload)
