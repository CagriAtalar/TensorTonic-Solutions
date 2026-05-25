import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    n = len(v)
    temp = np.zeros((n,n))
    for i in range(n):
        temp[i,i] = v[i]
    return temp
    
    pass
