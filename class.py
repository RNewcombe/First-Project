class stock:

    num_of_stk = 0
    raise_price = 2

    def __init__(self, name, prod, price):
        self.name = name
        self.prod = prod
        self.price = price

        Stock.num_of_stk += 1

    def apply_raise(self):
        self.price = int(self.price + self.raise_price)
    
    @classmethod
    def set_raise_price(cls, amount):
        cls.raise_price = amount

    stk_1 = Stock('Corona', 'Beer', 2)
    stk_2 = Stock('Twix', 'Bar', 1)

    Stock.set_raise_price(2.1)

    print(Stock.raise_price)
    print(stk_1.raise_price)