import sys
import interface as intfc

from constants import *
from maths import *


def main():
    if len(sys.argv) != 2:
        return ERROR_COMMAND_LINE_ARGS

    rc = EXIT_SUCCESS

    filename = sys.argv[1]
    degrees = list(map(int, input("Введите степень полинома: ").split()))

    points = intfc.read_from_file(filename)
    add_table(points, "Таблица")

    intfc.print_table(points)

    for j in range(len(degrees)):
        slae_matrix = find_slae_matrix(points, degrees[j])
        coefficients = get_polynomial_coefficients(slae_matrix)
        add_plot(coefficients, f"n = {degrees[j]}",
                 points[0].x, points[-1].x)

    draw_result()

    return rc


if __name__ == "__main__":
    sys.exit(main())
