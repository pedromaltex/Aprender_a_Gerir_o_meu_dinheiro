
def call_option(strike_price: float, stock_price:float, long=True) -> float:
    if not long:
        return -max(stock_price - strike_price, 0)
    return max(stock_price - strike_price, 0)

def put_option(strike_price: float, stock_price:float, long=True) -> float:
    if not long:
        return -max(strike_price - stock_price, 0)
    return max(strike_price - stock_price, 0)

