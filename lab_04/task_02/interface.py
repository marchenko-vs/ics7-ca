from maths import Point


def print_table(table: list):
    print("|-----------+------------+------------+------------|")
    print("|     X     |      Y     |     Z      |     Вес    |")
    print("|-----------+------------+------------+------------|")

    for i in range(len(table)):
        print(table[i])

    print("|-----------+------------+------------+------------|")


def read_from_file(filename: str) -> list:
    dots = list()

    with open(filename, "r") as f:
        line = f.readline()

        while line:
            x, y, z, weight = map(float, line.split())
            dots.append(Point(x, y, z, weight))
            line = f.readline()

    return dots

def add_table(table: list):
    table_x = [table[i].x for i in range(len(table))]
    table_y = [table[i].y for i in range(len(table))]
    table_z = [table[i].z for i in range(len(table))]
