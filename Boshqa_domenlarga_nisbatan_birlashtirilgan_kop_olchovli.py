import numpy as np


def func1(x):
    # function f(x)= 10 + sum_i(-x_i^2)
    # for 2D: f(x)= 10 - x1^2 - x2^2
    return 10 + np.sum(-1 * np.power(x, 2), axis=1)


def domain_unit_circle(x):
    # integration domain: sum of x^2 <= 1. 
    # For 2d, it's a unit circle; for 3d it's a unit sphere, etc
    # returns True for inside domain, False for outside

    return np.power(x, 2).sum() <= 1


def mc_integrate(func, func_domain, a, b, dim, n=1000):
    # Monte Carlo integration of given function over domain specified by func_domain
    # dim: dimensions of function

    # sample x
    x_list = np.random.uniform(a, b, (n, dim))

    # determine whether sampled x is inside or outside of domain and calculate its volume
    inside_domain = [func_domain(x) for x in x_list]
    frac_in_domain = sum(inside_domain) / len(inside_domain)
    domain = np.power(b - a, dim) * frac_in_domain

    # calculate expected value of func inside domain
    y = func(x_list)
    y_mean = y[inside_domain].sum() / len(y[inside_domain])

    # estimated integration
    integ = domain * y_mean

    return integ


print("For f(x)= 10 - x1\u00b2 - x2\u00b2, integrated over unit circle")
print(f"Monte Carlo solution: {mc_integrate(func1, domain_unit_circle, -2, 2, 2, 1000000): .3f}")
print(f"Analytical solution: 29.845")