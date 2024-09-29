from helpers.generator import GenCourierData
from helpers.generator import GenOrderData
from endpoints.sign_up_courier_post import CourierSignUp
from endpoints.sign_in_courier_post import CourierSignIn
from endpoints.create_order_post import OrderCreate
from endpoints.accept_orders_put import OrderAccept
from endpoints.get_order_by_track_get import GetOrder


class TestAcceptOrder:
    def test_accept_order_by_correct_data(self):
        gen_courier = GenCourierData()
        sign_up_courier = CourierSignUp(gen_courier.get_data_for_sign_up_courier())
        sign_up_courier.request()
        sign_in_courier = CourierSignIn(gen_courier.get_data_for_sign_in_courier())
        sign_in_courier.request()
        gen_order = GenOrderData()
        create_order = OrderCreate(gen_order.get_data_for_order())
        create_order.request()
        get_order = GetOrder(create_order.response.json()['track'])
        get_order.request()
        print(get_order.response.json())
        accept_order = OrderAccept(sign_in_courier.response.json()['id'], get_order.response.json()["order"]["id"])
        print(sign_in_courier.response.json()['id'])
        print(create_order.response.json()['track'])
        print(get_order.response.json()["order"]["id"])
        accept_order.request()
        print(accept_order.response.status_code)
        print(accept_order.response.text)
        print(accept_order.response.json())
        accept_order.check_status_code(200)