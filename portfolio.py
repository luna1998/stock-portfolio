class Portfolio:
    def _init_(self):
        self._stocks=[] #加下划线是因为设置成了private

    def buy(self,str name,int shares,float price):
        self._stocks.append((name,shares,price))

    def cost(self):
        return sum(
            shares * price for _, shares,price in self._stocks
        )
