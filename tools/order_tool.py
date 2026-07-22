import json


class OrderTool:

    def __init__(self):

        with open("data/orders.json", "r") as file:
            self.orders = json.load(file)

    def get_order(self, order_id):

        for order in self.orders:

            if order["order_id"] == str(order_id):
                return order

        return None