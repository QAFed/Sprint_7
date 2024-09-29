import pytest
from endpoints.sign_in_courier_post import CourierSignIn
from copy import copy


class TestSignInCourier:
    def test_courier_sign_in_by_correct_data(self, create_n_delete_courier):
        gen_courier_data = create_n_delete_courier
        courier_sign_in = CourierSignIn(gen_courier_data.get_data_for_sign_in_courier())
        courier_sign_in.request()
        courier_sign_in.check_status_code(200)
        assert courier_sign_in.response.json().get("id", None) is not None
        create_n_delete_courier.sidn_in_id = courier_sign_in.response.json()["id"]

    @pytest.mark.parametrize('kill_param', [
            "login",
            "password"
    ])
    def test_courier_not_sign_in_if_not_send_all_fields_are_required(self, kill_param, create_courier):
        gen_courier_data = create_courier
        mod_data = copy(gen_courier_data.get_data_for_sign_in_courier())
        mod_data[kill_param] = ""
        courier_sign_in = CourierSignIn(mod_data)
        courier_sign_in.request()
        courier_sign_in.check_status_code(400)
        courier_sign_in.check_response_json({
            "code": 400,
            "message": "Недостаточно данных для входа"
        })

    @pytest.mark.parametrize('not_correct_param', [
        "login",
        "password"
    ])
    def test_courier_not_sign_in_if_not_correct_param(self, not_correct_param, create_courier):
        gen_courier_data = create_courier
        mod_data = copy(gen_courier_data.get_data_for_sign_in_courier())
        mod_data[not_correct_param] = "%%%%"
        courier_sign_in = CourierSignIn(mod_data)
        courier_sign_in.request()
        courier_sign_in.check_status_code(404)
        courier_sign_in.check_response_json({
            "code": 404,
            "message": "Учетная запись не найдена"
        })
