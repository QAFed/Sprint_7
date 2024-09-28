import pytest
from endpoints.sign_in_courier_post import CourierSignIn
from endpoints.delete_courier_delete import CourierDelete
from helpers.generator import GenCourierData


@pytest.fixture
def delete_courier_after():
    gen_courier_data = GenCourierData()
    yield gen_courier_data
    sign_in_courier = CourierSignIn(gen_courier_data.get_data_for_sign_in_courier())
    sign_in_courier.request()
    delete_courier = CourierDelete(sign_in_courier.response.json()["id"])
    delete_courier.request()

