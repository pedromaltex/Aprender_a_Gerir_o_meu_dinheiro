def decreasing_continuously_compounded(i_v, annual_r, t):
    from math import exp
    """
    Calculates the future value of a lump-sum investment
    with annual compounding.
    
    Parameters:
        i_v (float): Initial investment (present value).
        annual_r (float): Annual interest rate (decimal).
        t (int): Number of years.
    
    Returns:
        float: Future value of the investment.
    """
    f = i_v * exp(-annual_r * t)
    return f

