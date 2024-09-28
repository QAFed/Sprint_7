from endpoints.sign_up_courier_post import CourierSignUp
from endpoints.sign_in_courier_post import CourierSignIn
from endpoints.delete_courier_delete import CourierDelete
from helpers.generator import GenCourierData


class TestSignInCourier:
    def test_courier_sign_in_by_correct_data(self):
        gen_courier_data = GenCourierData()
        courier_sign_up = CourierSignUp(gen_courier_data.get_data_for_sign_up_courier())
        courier_sign_up.request()
        courier_sign_in = CourierSignIn(gen_courier_data.get_data_for_sign_in_courier())
        courier_sign_in.request()
        courier_sign_in.check_status_code(200)
        print(courier_sign_up.payload)
        print(courier_sign_in.response.json())
        courier_delete = CourierDelete(courier_sign_in.response.json()["id"])
        courier_delete.request()
        courier_delete.check_status_code(200)
