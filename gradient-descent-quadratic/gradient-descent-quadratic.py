def gradient_descent_quadratic(a, b, c, x0, lr, steps):

    if steps <= 0:
        return x0

    grad_val = 2 * a * x0 + b
    x1 = x0 - lr * grad_val

    return gradient_descent_quadratic(a, b, c, x1, lr, steps - 1)