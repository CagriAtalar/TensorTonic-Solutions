import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    ortanca = sum(x)/len(x)
    s_kare = 0
    for i in range(len(x)):
        s_kare += (x[i] - ortanca) ** 2
    s_kare = s_kare / (len(x) -1)

    s = s_kare ** (1/2)

    return s_kare, s
    
    # Write code here
    pass