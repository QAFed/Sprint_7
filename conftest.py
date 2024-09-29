import pytest
from endpoints.sign_in_courier_post import CourierSignIn
from endpoints.delete_courier_delete import CourierDelete
from helpers.generator import GenCourierData
from endpoints.sign_up_courier_post import CourierSignUp
from helpers.generator import GenOrderData
from endpoints.create_order_post import OrderCreate
from endpoints.get_order_by_track_get import GetOrder

@pytest.fixture
def delete_courier_after():
    gen_courier_data = GenCourierData()
    yield gen_courier_data
    sign_in_courier = CourierSignIn(gen_courier_data.get_data_for_sign_in_courier())
    sign_in_courier.request()
    delete_courier = CourierDelete(sign_in_courier.response.json()["id"])
    delete_courier.request()

@pytest.fixture
def create_n_delete_courier():
    gen_courier_data = GenCourierData()
    courier_sign_up = CourierSignUp(gen_courier_data.get_data_for_sign_up_courier())
    courier_sign_up.request()
    sign_in_courier = CourierSignIn(gen_courier_data.get_data_for_sign_in_courier())
    sign_in_courier.request()
    gen_courier_data.sidn_in_id = sign_in_courier.response.json()["id"]
    yield gen_courier_data
    delete_courier = CourierDelete(sign_in_courier.response.json()["id"])
    delete_courier.request()

@pytest.fixture
def create_courier():
    gen_courier_data = GenCourierData()
    courier_sign_up = CourierSignUp(gen_courier_data.get_data_for_sign_up_courier())
    courier_sign_up.request()
    return gen_courier_data

@pytest.fixture
def create_n_sign_in():
    gen_courier_data = GenCourierData()
    courier_sign_up = CourierSignUp(gen_courier_data.get_data_for_sign_up_courier())
    courier_sign_up.request()
    sign_in_courier = CourierSignIn(gen_courier_data.get_data_for_sign_in_courier())
    sign_in_courier.request()
    gen_courier_data.sidn_in_id = sign_in_courier.response.json()["id"]
    return gen_courier_data

@pytest.fixture
def create_order():
    gen_data = GenOrderData()
    order_create = OrderCreate(gen_data.get_data_for_order())
    order_create.request()
    get_order = GetOrder(order_create.response.json()['track'])
    get_order.request()
    return get_order.response.json()["order"]["id"]


@pytest.fixture
def create_order_track():
    gen_data = GenOrderData()
    order_create = OrderCreate(gen_data.get_data_for_order())
    order_create.request()
    return order_create.response.json()['track']