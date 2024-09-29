
from endpoints.get_order_by_track_get import GetOrder

class TestOrderGetByNum:
    def test_order_get_by_num_success(self, create_order_track):
        order_track = create_order_track
        print(order_track)
        get_order = GetOrder(order_track)
        get_order.request()
        print(get_order.response.json())
        get_order.check_status_code(200)
        print(get_order.response.json())
        assert get_order.response.json().get("order",None).get("track",None) == order_track

    def test_order_get_by_num_fail_if_number_not_send(self):
        order_track = ''
        get_order = GetOrder(order_track)
        get_order.request()
        print(get_order.response.json())
        get_order.check_status_code(400)
        print(get_order.response.json())
        get_order.check_response_json({
            "code": 400,
            "message": "Недостаточно данных для поиска"
        })

    def test_order_get_by_num_fail_if_number_not_exist(self):
        order_track = '0000'
        get_order = GetOrder(order_track)
        get_order.request()
        print(get_order.response.json())
        get_order.check_status_code(404)
        print(get_order.response.json())
        get_order.check_response_json({
            "code": 404,
            "message": "Заказ не найден"
        })