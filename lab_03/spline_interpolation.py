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
        teta_cur = (fi - h1 * teta_arr[i - 1]) \
                   / (h1 * ksi_arr[i - 1] + 2 * (h2 + h1))

        ksi_arr.append(ksi_cur)
        teta_arr.append(teta_cur)

    c[-1] = teta_arr[-1]

    for i in range(size - 2, 0, -1):
        c[i - 1] = ksi_arr[i] * c[i] + teta_arr[i]

    return c


def calc_B_and_D(x_arr: list, y_arr: list, C: list,
                 table: list, flag: int) -> tuple:
    B = []
    D = []

    for i in range(1, len(x_arr) - 1):
        h = x_arr[i] - x_arr[i - 1]

        B.append((y_arr[i] - y_arr[i - 1]) / 
                 h - (h * (C[i] + 2 * C[i - 1])) / 3)
        D.append((C[i] - C[i - 1]) / (3 * h))

    h = x_arr[-1] - x_arr[-2]

    B.append((y_arr[-1] - y_arr[-2]) / h - (h * 2 * C[-1]) / 3)

    if flag == 3:
        np, np_derivative = new_int.newton_polynomial(copy.deepcopy(table),
                                                     3, y_arr[-1])
        D.append(np_derivative - C[-1] / (3 * h))
    else:
        D.append(- C[-1] / (3 * h))

    return B, D


def calculate_koefs_spline(x_arr: list, y_arr: list, 
                           table: list, flag: int) -> tuple:
    A = calc_a(y_arr)
    C = calc_c(x_arr, y_arr, table, flag)
    B, D = calc_B_and_D(x_arr, y_arr, C, table, flag)

    return A, B, C, D


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

    coefficients = calculate_koefs_spline(x_arr, y_arr, table, flag)

    index = find_index(x_arr, x)

    return count_polynom(x, x_arr, index, coefficients)
