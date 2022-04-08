import copy
import spline
import sys
import interface as ui
import newtonPolynomial as newton

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

    if (rc == EXIT_SUCCESS):
        rc, flag = ui.scan_option()

        if (rc == EXIT_SUCCESS):
            np, np_derivative = newton.newton_polynomial(copy.deepcopy(table), 
                                                         3, x)
            spl = spline.spline(table, x, flag)

            print('\nИнтерполяция сплайнами = {:.3f}'.format(spl))
            print('Интреполяция полиномом Ньютона = {:.3f}'.format(np))

    return EXIT_FAILURE

if __name__ == "__main__":
    sys.exit(main())
