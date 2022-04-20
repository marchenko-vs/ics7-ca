from maths import Point


def print_table(table: list):
    print("|-----------+------------+------------|")
    print("|     X     |      Y     |     Вес    |")
    print("|-----------+------------+------------|")

    for i in range(len(table)):
        print(table[i])

    print("|-----------+------------+------------|")


def read_from_file(filename: str) -> list:
    dots = list()

    with open(filename, "r") as f:
        line = f.readline()

        while line:
            x, y, weight = map(float, line.split())
            dots.append(Point(x, y, weight))
            line = f.readline()

    return dots
