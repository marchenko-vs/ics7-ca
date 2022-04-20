from matplotlib.pyplot import *
from numpy import linspace
from constants import *
from maths import *
import interface as intfc
import sys


def main():
    if len(sys.argv) != 2:
        return ERROR_COMMAND_LINE_ARGS

    filename = sys.argv[1]
    degrees = int(input("Введите степень полинома: "))

    points = intfc.read_from_file(filename)
    intfc.add_table(points)

    intfc.print_table(points)

    slae_matrix = find_slae_matrix_3d(points, degrees)
    coefficients = method_gauss(slae_matrix)
    fig = figure()
    ax = fig.add_subplot(111, projection='3d')

    table_x = [points[i].x for i in range(len(points))]
    table_y = [points[i].y for i in range(len(points))]
    table_z = [points[i].z for i in range(len(points))]

    ax.scatter(table_x, table_y, table_z, c='red')

    x = list(linspace(min(table_x), max(table_x), 20))
    y = list(linspace(min(table_y), max(table_y), 20))

    res_x = []
    res_y = []
    res_z = []

    for elx in x:
        for ely in y:
            elz = 0
            i = 0
            for k in range(0, degrees + 1):
                for l in range(0, k + 1):
                    elz += coefficients[i] * elx ** (k - l) * ely ** l
                    i += 1
            res_x.append(elx)
            res_y.append(ely)
            res_z.append(elz)
    ax.plot_trisurf(res_x, res_y, res_z, color='green', alpha=0.5)

    ax.set_title('График функции', fontsize=17)

    ax.set_xlabel('X', fontsize=15)
    ax.set_ylabel('Y', fontsize=15)
    ax.set_zlabel('Z', fontsize=15)

    show()


if __name__ == "__main__":
    sys.exit(main())
