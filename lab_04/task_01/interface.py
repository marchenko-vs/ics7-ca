from constants import *
from maths import Point


def scan_dots(filename: str) -> list:
    dots = list()

    try:
        with open(filename, "r") as f:
            line = f.readline()

            while line:
                x, y, weight = map(float, line.split())
                dots.append(Point(x, y, weight))
                line = f.readline()
    except FileNotFoundError:
        return ERROR_INCORRECT_FILE_NAME

    return dots


def print_table(table: list):
    print("+-----------+------------+------------+")
    print("|     X     |      Y     |     Вес    |")
    print("+-----------+------------+------------+")

    for i in range(len(table)):
        print(table[i])
        print("+-----------+------------+------------+")
