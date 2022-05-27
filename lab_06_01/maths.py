from numpy.polynomial.legendre import leggauss
from numpy import linspace
from math import sqrt


def t_x(t, a, b):
    return (b + a) / 2 + (b - a) * t / 2


def function(x, y):
    return sqrt(x * x + y * y)


def integral(f, y):
    return lambda x: f(x, y)


def g_function(y):
    return 1 - sqrt(1 - y * y), 1 + sqrt(1 - y * y)


def simpson(f, a, b, num):
    if num < 3 or num & 1 == 0:
        raise ValueError

    h = (b - a) / (num - 1)
    x = a
    res = 0

    for i in range((num - 1) // 2):
        res += f(x) + 4 * f(x + h) + f(x + 2 * h)
        x += 2 * h

    return res * (h / 3)


def gauss(f, a, b, num):
    args, coefficients = leggauss(num)
    res = 0

    for i in range(num):
        res += (b - a) / 2 * coefficients[i] * f(t_x(args[i], a, b))

    return res


def solution(hy, hx):
    y_arr = list(linspace(-1, 1, hy))
    x_arr = []

    for y in y_arr:
        xa, xb = g_function(y)
        fx = integral(function, y)
        x_arr.append(gauss(fx, xa, xb, hx))

    return y_arr, x_arr


def f(x, x_arr, y_arr_):
    i = 0

    while i < len(x_arr) and abs(x_arr[i] - x) > 1e-6:
        i += 1

    return y_arr_[i]
