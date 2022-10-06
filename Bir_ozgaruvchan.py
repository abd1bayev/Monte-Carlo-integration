import numpy as np


def func1(x):
    # funksiya f(x)=x^2
    return x ** 2


def func1_int(a, b):
    # f(x) integralining analitik yechimi
    return (1 / 3) * (b ** 3 - a ** 3)


def mc_integrate(func, a, b, n=1000):
    # a dan b gacha berilgan funksiyaning x1 va x2 o'rtasidagi Monte-Karlo integratsiyasi

    vals = np.random.uniform(a, b, n)
    y = [func(val) for val in vals]

    y_mean = np.sum(y) / n
    integ = (b - a) * y_mean

    return integ


print(f"Monte Carlo solution: {mc_integrate(func1, -2, 2, 500000): .4f}")
print(f"Analytical solution: {func1_int(-2, 2): .4f}")
