import pytest
from orders_methods import OrderMethods
from generators import generate_order

class TestOrder:
    @pytest.mark.parametrize("colors", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order(self, colors):
        order_data = generate_order(colors=colors)
        response = OrderMethods.create_order(order_data)
        assert response.status_code == 201
        assert "track" in response.json()
        track = response.json()["track"]
        OrderMethods.cancel_order(track)
