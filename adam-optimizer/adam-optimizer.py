import numpy as np

def adam_step(param, grad, m, v, t,
              lr=1e-3,
              beta1=0.9,
              beta2=0.999,
              eps=1e-8):

    for i in range(len(param)):

        # Momentum
        m[i] = beta1 * m[i] + (1 - beta1) * grad[i]

        # RMS term
        v[i] = beta2 * v[i] + (1 - beta2) * (grad[i] ** 2)

        # Bias correction
        m_hat = m[i] / (1 - beta1 ** t)
        v_hat = v[i] / (1 - beta2 ** t)

        # Parameter update
        param[i] = param[i] - lr * m_hat / (np.sqrt(v_hat) + eps)

    return param, m, v