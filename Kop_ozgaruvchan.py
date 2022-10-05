import numpy as np


def func1(x):
    # function f(x)= 10 + sum_i(-x_i^2)
    # for 2D: f(x)= 10 - x1^2 - x2^2
    return 10 + np.sum(-1 * np.power(x, 2), axis=1)


def mc_integrate(func, a, b, dim, n=1000):
    # Monte Carlo integration of given function over domain from a to b (for each parameter)
    # dim: dimensions of function

    x_list = np.random.uniform(a, b, (n, dim))
    y = func(x_list)

    y_mean = y.sum() / len(y)
    domain = np.power(b - a, dim)

    integ = domain * y_mean

    return integ


# Examples
print("For f(x)= 10 - x1\u00b2 - x2\u00b2, integrated from -2 to 2 (for all x's)")
print(f"Monte Carlo solution for : {mc_integrate(func1, -2, 2, 2, 1000000): .3f}")
print(f"Analytical solution: 117.333")

print("For f(x)= 10 - x1\u00b2 - x2\u00b2 - x3\u00b2, integrated from -2 to 2 (for all x's)")
print(f"Monte Carlo solution: {mc_integrate(func1, -2, 2, 3, 1000000): .3f}")
print(f"Analytical solution: 384.000")