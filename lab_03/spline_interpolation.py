import copy
import newton_interpolation as new_int


def calc_a(y_arr: list) -> list:
    return y_arr[:-1]


def calc_c(x_arr: list, y_arr: list,
           table: list, flag: int) -> list:
    size = len(x_arr)

    c = [0] * (size - 1)

    if flag == 2 or flag == 3:
        np, np_derivative = new_int.newton_polynomial(copy.deepcopy(table),
                                                      3, 0)
        c[0] = np_derivative

    ksi_arr = [0, 0]
    teta_arr = [0, 0]

    for i in range(2, size):
        h1 = x_arr[i] - x_arr[i - 1]
        h2 = x_arr[i - 1] - x_arr[i - 2]

        fi = 3 * ((y_arr[i] - y_arr[i - 1]) / h1 -
                  (y_arr[i - 1] - y_arr[i - 2]) / h2)

        ksi_cur = - h1 / (h2 * ksi_arr[i - 1] + 2 * (h2 + h1))
        teta_cur = (fi - h1 * teta_arr[i - 1]) / (h1 * ksi_arr[i - 1] +
                                                  2 * (h2 + h1))

        ksi_arr.append(ksi_cur)
        teta_arr.append(teta_cur)

    c[-1] = teta_arr[-1]

    for i in range(size - 2, 0, -1):
        c[i - 1] = ksi_arr[i] * c[i] + teta_arr[i]

    return c


def calc_b_and_d(x_arr: list, y_arr: list, c: list,
                 table: list, flag: int) -> tuple:
    b = []
    d = []

    for i in range(1, len(x_arr) - 1):
        h = x_arr[i] - x_arr[i - 1]

        b.append((y_arr[i] - y_arr[i - 1]) /
                 h - (h * (c[i] + 2 * c[i - 1])) / 3)
        d.append((c[i] - c[i - 1]) / (3 * h))

    h = x_arr[-1] - x_arr[-2]

    b.append((y_arr[-1] - y_arr[-2]) / h - (h * 2 * c[-1]) / 3)

    if flag == 3:
        np, np_derivative = new_int.newton_polynomial(copy.deepcopy(table),
                                                      3, y_arr[-1])
        d.append(np_derivative - c[-1] / (3 * h))
    else:
        d.append(- c[-1] / (3 * h))

    return b, d


def calc_coefficients(x_arr: list, y_arr: list,
                      table: list, flag: int) -> tuple:
    a = calc_a(y_arr)
    c = calc_c(x_arr, y_arr, table, flag)
    b, d = calc_b_and_d(x_arr, y_arr, c, table, flag)

    return a, b, c, d


def find_index(x_arr: list, x: float) -> int:
    size = len(x_arr)
    index = 1

    while index < size and x_arr[index] < x:
        index += 1

    return index - 1


def count_polynom(x: float, x_arr: list, index: int,
                  coefficients: tuple) -> float:
    h = x - x_arr[index]
    y = 0

    for i in range(4):
        y += coefficients[i][index] * (h ** i)

    return y


def spline(table: list, x: float, flag: int) -> float:
    x_arr = [i[0] for i in table]
    y_arr = [i[1] for i in table]

    coefficients = calc_coefficients(x_arr, y_arr, table, flag)

    index = find_index(x_arr, x)

    return count_polynom(x, x_arr, index, coefficients)
