import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    total = 0
    if sum(p) != 1:
        raise ValueError
    for i in range(len(x)):
        total += x[i] * p[i]
    return total
    # Write code here
    pass
