import pytest
from portfolio import Portfolio

def test_empty_portfolio():
    p=Portfolio()
    assert p.cost()==0.0

def test_buy_one_stock():
    p = Portfolio()
    p.buy("IBM", 100, 176.48)
    assert p.cost() == 17648.0

def test_buy_two_stock():
    p = Portfolio()
    p.buy("IBM", 100, 176.48)
    p.buy("HPQ", 100, 36.15)
    assert p.cost() == 21263.0

#def test_not_enough_arguments_to_buy():
   # p=Portfolio()
    #try:
    #    p.buy("IBM")
    #excpet TypeError:
     #   pass
    #else:
     #  assert False,"we didn't get an exception!"
    
def test_not_enough_arguments_to_buy():
    p=Portfolio()
    with pytest.raises(TypeError):
        p.buy("IBM",price=100)
#除非有typeError,不然就会通过，就和上面try excep原理一样
