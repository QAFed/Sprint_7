import pytest
from endpoints.create_order_post import OrderCreate
from helpers.generator import GenOrderData


class TestOrderCreate:
    def test_order_create_by_correct_data(self):
        gen_data = GenOrderData()
        order_create = OrderCreate(gen_data.get_data_for_order())
        order_create.request()
        order_create.check_status_code(201)
        assert order_create.response.json().get("track", None) is not None

    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"]
    ])
    def test_order_create_variate_color(self, color):
        gen_data = GenOrderData()
        mod_data = gen_data.get_data_for_order()
        mod_data['color'] = color
        order_create = OrderCreate(mod_data)
        order_create.request()
        order_create.check_status_code(201)
