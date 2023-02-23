import datetime


class Order:
    def __init__(self, price: int, operation: str, currency_name="USDT"):
        self.currency_name = currency_name
        self.operation = operation
        self.price = price if price > 0 else 1
        self.created_time = datetime.datetime.now()
        self.id = hash(self)
