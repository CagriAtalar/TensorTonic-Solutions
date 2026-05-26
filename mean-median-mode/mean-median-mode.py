import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """

    n = len(x)

    # Mean
    mean = sum(x) / n

    # Median
    x_sorted = sorted(x)

    if n % 2 == 0:
        median = (x_sorted[n//2 - 1] + x_sorted[n//2]) / 2
    else:
        median = x_sorted[n//2]

    # Mode
    counts = Counter(x)
    mode = counts.most_common(1)[0][0]

    return mean, median, mode