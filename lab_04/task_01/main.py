import sys
import interface as intfc

from constants import *
from maths import *


def main():
    if len(sys.argv) != 2:
        print('Ошибка: должно быть два аргумента командной строки.')

        return ERROR_COMMAND_LINE_ARGS

    filename = sys.argv[1]

    points = intfc.scan_dots(filename)

    if points == ERROR_INCORRECT_FILE_NAME:
        print('Ошибка: файл не существует.')

        return ERROR_INCORRECT_FILE_NAME

    try:
        degree_list = list(map(int, input("Введите степени полинома: ").split()))
    except ValueError:
        print('Ошибка: степени должны быть целыми числами.')

        return ERROR_INCORRECT_DATA_TYPE

    add_dots(points)

    intfc.print_table(points)

    for i in range(len(degree_list)):
        linear_system_matrix = find_linear_system_matrix(points, degree_list[i])
        coefficients = get_polynomial_coefficients(linear_system_matrix)
        add_approximation_function(coefficients, points[0].x, points[-1].x, degree_list[i])

    draw_result()

    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
