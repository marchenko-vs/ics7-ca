from constants import *
from sympy import symbols, diff


def divided_difference(x_0: float, y_0: float, x_1: float, y_1: float) -> float:
    if abs(x_0 - x_1) > EPS:
        return (y_0 - y_1) / (x_0 - x_1)


def search_index(table: list, x: float, n: int) -> int:
    index = 0

    for i in table:
        if i[0] > x:
            break
        index += 1

    if index >= len(table) - n:
        return len(table) - n - 1

    l_border = index
    r_border = index

    while n > 0:
        if r_border - index == index - l_border:
            if l_border > 0:
                l_border -= 1
            else:
                r_border += 1
        else:
            if r_border < len(table) - 1:
                r_border += 1
            else:
                l_border -= 1
        n -= 1

    return l_border


def newton_polynomial(table: list, degree: int, argument: float) -> tuple:
    index = search_index(table, argument, degree)
    np = str(table[index][1])

    for i in range(degree):
        for j in range(degree - i):
            table[index + j][1] = divided_difference(
                table[index + j][0], table[index + j][1],
                table[index + j + i + 1][0], table[index + j + 1][1])

        mult = "(" + str(table[index][1]) + ")"

        for j in range(i + 1):
            mult += " * (x - " + str(table[index + j][0]) + ")"

        np += " + " + mult

    x = symbols('x', real=True)

    return eval(np, {},
                {"x": argument}), diff(diff(eval(np))).subs({x: argument})
