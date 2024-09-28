from endpoints.create_order import OrderCreate
from helpers.generator import GenOrderData


class TestOrderCreate:
    def test_order_create_by_correct_data(self):
        gen_data = GenOrderData()
        order_create = OrderCreate(gen_data.get_data_for_order())
        order_create.request()
        order_create.check_status_code(201)
        print(order_create.response.json())
