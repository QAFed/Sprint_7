
from endpoints.delete_courier_delete import CourierDelete


class TestDeleteCourier:
    def test_courier_delete_success(self, create_n_sign_in):
        delete_courier = CourierDelete(create_n_sign_in.sidn_in_id)
        delete_courier.request()
        delete_courier.check_status_code(200)
        delete_courier.check_response_json({
            "ok": True
        })

    def test_courier_not_delete_if_courier_id_not_exist(self):
        delete_courier = CourierDelete("01010")
        delete_courier.request()
        delete_courier.check_status_code(404)
        delete_courier.check_response_json({
            "code": 404,
            "message": "Курьера с таким id нет."
        })

    def test_courier_not_delete_if_id_not_send(self):
        delete_courier = CourierDelete("")
        delete_courier.request()
        delete_courier.check_status_code(404)
        delete_courier.check_response_json({
            "code": 404,
            "message": "Not Found."
        })
