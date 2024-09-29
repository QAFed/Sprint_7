import pytest
from copy import copy
from endpoints.sign_up_courier_post import CourierSignUp
from helpers.generator import GenCourierData


class TestAddCourier:
    def test_courier_sign_up_by_correct_data(self, delete_courier_after):
        gen_courier_data = delete_courier_after
        courier_sign_up = CourierSignUp(gen_courier_data.get_data_for_sign_up_courier())
        courier_sign_up.request()
        print(courier_sign_up.response.json())
        print(courier_sign_up.response.status_code)
        courier_sign_up.check_status_code(201)
        courier_sign_up.check_response_json({
            "ok":True
        })

    def test_courier_not_sign_up_second_with_same_data(self):
        gen_courier_data = GenCourierData()
        courier_sign_up = CourierSignUp(gen_courier_data.get_data_for_sign_up_courier())
        courier_sign_up.request()
        courier_sign_up.request()
        courier_sign_up.check_status_code(409)
        courier_sign_up.check_response_json({
            "code": 409,
            "message": "Этот логин уже используется. Попробуйте другой."
        })
    @pytest.mark.parametrize('kill_param',[
            "login",
            "password"
    ])
    def test_courier_not_sign_up_if_not_send_all_fields_are_required(self, kill_param):
        gen_courier_data = GenCourierData()
        mod_gen_data = copy(gen_courier_data.get_data_for_sign_up_courier())
        mod_gen_data.pop(kill_param, None)
        courier_sign_up = CourierSignUp(mod_gen_data)
        print(mod_gen_data)
        courier_sign_up.request()
        courier_sign_up.check_status_code(400)
        print(courier_sign_up.response.json())
        courier_sign_up.check_response_json({
            'code': 400,
            'message': 'Недостаточно данных для создания учетной записи'
        })