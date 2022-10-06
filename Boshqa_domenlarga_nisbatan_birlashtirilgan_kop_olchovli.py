import numpy as np

def func1(x):
    # funksiya f(x)= 10 + sum_i(-x_i^2) 6 
    # 2D uchun: f(x)= 10 - x1^2 - x2^2
    return 10 + np.sum(-1 * np.power(x, 2), axis=1)

def domain_unit_circle(x):
# integratsiya domeni: x^2 <= 1 yig'indisi. 12 
# 2d uchun bu birlik doira; 3D uchun bu birlik shar va boshqalar 13 
# ichki domen uchun True, tashqarisi uchun False qiymatini qaytaradi

    return np.power(x, 2).sum() <= 1

def mc_integrate(func, func_domain, a, b, dim, n=1000):
    # Func_domain tomonidan belgilangan domen orqali berilgan funksiyaning Monte-Karlo integratsiyasi 20 21 
    # xira: funktsiya o'lchamlari
    # namuna x
    x_list = np.random.uniform(a, b, (n, dim))

     # namunali x domen ichida yoki tashqarisida ekanligini aniqlang va uning hajmini hisoblang
    inside_domain = [func_domain(x) for x in x_list]
    frac_in_domain = sum(inside_domain) / len(inside_domain)
    domain = np.power(b - a, dim) * frac_in_domain

    # domen ichidagi funcning kutilgan qiymatini hisoblang
    y = func(x_list)
    y_mean = y[inside_domain].sum() / len(y[inside_domain])

    # taxminiy integratsiya
    integ = domain * y_mean

    return integ


print("For f(x)= 10 - x1\u00b2 - x2\u00b2, integrated over unit circle")
print(f"Monte Carlo solution: {mc_integrate(func1, domain_unit_circle, -2, 2, 2, 1000000): .3f}")
print(f"Analytical solution: 29.845")
