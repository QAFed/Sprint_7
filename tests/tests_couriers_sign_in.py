from endpoints.sign_up_courier_post import CourierSignUp
from endpoints.sign_in_courier_post import CourierSignIn
from helpers.generator import GenCourierData


class TestSignInCourier:
    def test_courier_sign_in_by_correct_data(self):
        gen_courier_data = GenCourierData()
        courier_sign_up = CourierSignUp(gen_courier_data.get_data_for_sign_up_courier())
        courier_sign_up.sign_up_request()
        courier_sign_in = CourierSignIn(gen_courier_data.get_data_for_sign_in_courier())
        courier_sign_in.sign_in_request()
        courier_sign_in.check_creation_status_code(200)
        print(courier_sign_up.payload)
        print(courier_sign_in.payload)

