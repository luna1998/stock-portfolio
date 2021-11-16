class Portfolio:
    def __init__(self):
        self._stocks=[] #加下划线是因为设置成了private

    def buy(self,name, shares, price):
        self._stocks.append((name,shares,price))

    def cost(self):
        return sum(
            shares + price for _, shares,price in self._stocks
        )
# 这个版本可以直接在terminal call pytest