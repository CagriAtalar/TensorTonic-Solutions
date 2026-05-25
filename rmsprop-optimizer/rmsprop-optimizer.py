import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):

    w = np.array(w, dtype=float)
    g = np.array(g, dtype=float)
    s = np.array(s, dtype=float)

    for i in range(len(s)):

        s[i] = beta * s[i] + (1 - beta) * (g[i] ** 2)

        w[i] = w[i] - (lr * g[i]) / (np.sqrt(s[i]) + eps)

    return w, s