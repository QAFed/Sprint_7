from endpoints.order_accept_put import OrderAccept


class TestAcceptOrder:
    def test_accept_order_by_correct_data(self, create_n_delete_courier, create_order):
        gen_courier = create_n_delete_courier
        order_id = create_order
        accept_order = OrderAccept(gen_courier.sidn_in_id, order_id)
        accept_order.request()
        accept_order.check_status_code(200)
        accept_order.check_response_json({
            "ok": True
        })

    def test_accept_order_not_done_if_courier_id_not_send(self, create_order):
        order_id = create_order
        accept_order = OrderAccept("", order_id)
        accept_order.request()
        accept_order.check_status_code(400)
        accept_order.check_response_json({
            "code": 400,
            "message": "Недостаточно данных для поиска"
        })

    def test_accept_order_not_done_if_courier_id_not_exist(self, create_order):
        order_id = create_order
        accept_order = OrderAccept("1", order_id)
        accept_order.request()
        accept_order.check_status_code(404)
        accept_order.check_response_json({
            "code": 404,
            "message": "Курьера с таким id не существует"
        })

    def test_accept_order_not_done_if_number_not_send(self, create_n_delete_courier):
        gen_courier = create_n_delete_courier
        accept_order = OrderAccept(gen_courier.sidn_in_id, "")
        accept_order.request()
        accept_order.check_status_code(400)
        accept_order.check_response_json({
            "code": 400,
            "message": "Недостаточно данных для поиска"
        })

    def test_accept_order_not_done_if_number_wrong(self, create_n_delete_courier):
        gen_courier = create_n_delete_courier
        accept_order = OrderAccept(gen_courier.sidn_in_id, "0000")
        accept_order.request()
        accept_order.check_status_code(404)
        accept_order.check_response_json({
            "code": 404,
            "message": "Заказа с таким id не существует"
        })
