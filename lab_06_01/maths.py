from numpy.polynomial.legendre import leggauss
from numpy import linspace
from math import sqrt

EPS = 1e-6


def t_x(t, a, b):
    return (b + a) / 2 + (b - a) * t / 2


def function(x, y):
    return sqrt(x * x + y * y)


def integral(f, y):
    return lambda x: f(x, y)


def g_function(y):
    return 1 - sqrt(1 - y * y), 1 + sqrt(1 - y * y)


def simpson_method(f, a, b, num):
    if num < 3 or num & 1 == 0:
        raise ValueError

    h = (b - a) / (num - 1)
    x = a
    res = 0

    for i in range((num - 1) // 2):
        res += f(x) + 4 * f(x + h) + f(x + 2 * h)
        x += 2 * h

    return res * (h / 3)


def gauss_method(f, a, b, num) -> float:
    args, coefficients = leggauss(num)
    res = 0

    for i in range(num):
        res += (b - a) / 2 * coefficients[i] * f(t_x(args[i], a, b))

    return res


def find_solution(hx: float, hy: float) -> tuple:
    y_arr = list(linspace(-1, 1, int(hy)))
    x_arr = []

    for y in y_arr:
        xa, xb = g_function(y)
        fx = integral(function, y)
        x_arr.append(gauss_method(fx, xa, xb, hx))

    return y_arr, x_arr


def lambda_function(x: float, x_array: list, y_array: list) -> float:
    i = 0

    while i < len(x_array) and abs(x_array[i] - x) > EPS:
        i += 1

    return y_array[i]
