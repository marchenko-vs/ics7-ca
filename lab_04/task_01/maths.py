from numpy import arange
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x: float = 0, y: float = 0, weight: float = 1):
        self.x = x
        self.y = y
        self.weight = weight

    def __str__(self):
        return f"|{self.x:^10.2f} | {self.y:^10.2f} | {self.weight:^10.2f} |"


def add_dots(table: list):
    table_x = [table[i].x for i in range(len(table))]
    table_y = [table[i].y for i in range(len(table))]

    plt.plot(table_x, table_y, 'ro', label='Табличная функция')


def get_coefficient(dots: list, degree: int) -> float:
    coefficient = 0

    for i in range(len(dots)):
        coefficient += dots[i].weight * (dots[i].x ** degree)

    return coefficient


def append_right_side(matrix: list, dots: list):
    for i in range(len(matrix)):
        res = 0

        for j in range(len(dots)):
            res += dots[j].weight * dots[j].y * (dots[j].x ** i)

        matrix[i].append(res)


def find_linear_system_matrix(dots: list, degree: int) -> list:
    matrix = [[get_coefficient(dots, j + i) for i in range(degree + 1)] for j in range(degree + 1)]
    append_right_side(matrix, dots)

    return matrix


def get_polynomial_coefficients(matrix: list) -> list:
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                continue

            multiplier = matrix[j][i] / matrix[i][i]

            for k in range(0, len(matrix) + 1):
                matrix[j][k] -= multiplier * matrix[i][k]

    for i in range(len(matrix)):
        multiplier = matrix[i][i]

        for j in range(len(matrix[i])):
            matrix[i][j] /= multiplier

    return [matrix[i][-1] for i in range(len(matrix))]


def add_approximation_function(coefficients: list, start: float, end: float, degree: int):
    my_x = list()
    my_y = list()
    step = (end - start) / 1000

    for x in arange(start, end + step, step):
        my_x.append(x)
        y = 0

        for i in range(len(coefficients)):
            y += coefficients[i] * x ** i

        my_y.append(y)

    plt.plot(my_x, my_y, 'g', label=f'Кривая (n = {degree})')


def draw_result():
    plt.title('Графики функций', fontsize=15)
    plt.legend()

    plt.xlabel('X', fontsize=13)
    plt.ylabel('Y', fontsize=13)

    plt.grid()
    plt.show()
