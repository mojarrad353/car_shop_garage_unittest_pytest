
from carshop import Garage
from carshop import Garage
import pytest


@pytest.fixture
def cart():
    return Garage(6)


def test_can_add_item_to_cart(cart):
    cart.add_car("ferarri")
    assert cart.get_car_count() == 1

def test_when_item_added_then_cart_contains_item(cart):
    cart.add_car("ford")
    assert "ford" in cart.get_cars()


def test_when_add_more_than_max_items_should_fail(cart):
    for _ in range(6):
        cart.add_car("ford")
    with pytest.raises(OverflowError):
        cart.add_car("ford")


def test_can_get_total_price(cart):
    cart.add_car("ford")
    cart.add_car("ferarri")
    price_list = {"ford": 1.2, "ferarri": 3.1}
    total_price = cart.get_total_value(price_list)
    assert total_price == 4.3
    
