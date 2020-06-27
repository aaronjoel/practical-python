class Stock:

    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self.shares = shares if shares > 0 else 0
        self.price = price
    
    def cost(self) -> float:
        return self.shares * self.price
    
    def sell(self, nshares) -> None:
        left = self.shares - nshares
        
        if left >= 0:
            self.shares = left

        
class MyStock(Stock):

    def __init__(self, name, shares, price, factor):
        # Check the call to super `super` and `__init__`
        super().__init__(name, shares, price)
        self.factor = factor

    def cost(self):
        # Check the call to `super`
        return self.factor * super().cost()
