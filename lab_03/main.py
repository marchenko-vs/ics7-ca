import copy
import interface as ui
import newton_interpolation as new_int
import spline_interpolation as spl_int
import sys

from constants import *


def main():
    table = [[0, 0],
             [1, 0.496],
             [2, 0.986],
             [3, 1.102],
             [4, 0.972],
             [5, 0.754],
             [6, 0.539],
             [7, 0.364],
             [8, 0.236],
             [9, 0.148],
             [10, 0.091]]

    ui.print_table(table)

    rc, x = ui.scan_argument()

    if rc == EXIT_SUCCESS:
        rc, condition = ui.scan_condition()

        if rc == EXIT_SUCCESS:
            np, np_derivative = new_int.newton_polynomial(copy.deepcopy(table),
                                                          3, x)
            spline = spl_int.spline(table, x, condition)

            print('\nИнтерполяция сплайнами = {:.3f}'.format(spline))
            print('Интерполяция полиномом Ньютона = {:.3f}'.format(np))

    return rc


if __name__ == "__main__":
    sys.exit(main())
