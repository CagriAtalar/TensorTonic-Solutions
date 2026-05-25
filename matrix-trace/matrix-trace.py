import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    n = len(A)
    total = 0

    for i in range(n):
        total += A[i][i]

    return total