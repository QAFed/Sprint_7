from endpoints.get_list_orders import GetOrdersList


class TestOrdersList:
    def test_get_all_orders_list(self):
        get_orders_list=GetOrdersList(3)
        get_orders_list.request()
        get_orders_list.check_status_code(200)