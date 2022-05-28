import interface

TABLE = []


def left_formula(y):
    global TABLE

    res = ["-"]

    for i in range(1, len(y)):
        r = y[i] - y[i - 1]
        res.append(str(round(r, 3)))

    TABLE.append(res)


def centre_formula(y):
    global TABLE

    res = ["-"]

    for i in range(1, len(y) - 1):
        r = (y[i + 1] - y[i - 1]) / 2
        res.append(str(round(r, 3)))
    res.append("-")

    TABLE.append(res)


def right_formula(y):
    global TABLE

    res = []

    for i in range(len(y) - 2):
        s1 = y[i + 1] - y[i]
        s2 = (y[i + 2] - y[i]) / 2
        r = s1 * 2 - s2
        res.append(str(round(r, 3)))

    res.append("-")
    res.append("-")

    TABLE.append(res)


def leveling_based_formula(x, y):
    global TABLE

    res = []

    for i in range(len(y) - 1):
        s1 = (1 / y[i] - 1 / y[i + 1]) / (1 / x[i] - 1 / x[i + 1])
        r = y[i] * y[i] * s1 / (x[i] * x[i])
        res.append(str(round(r, 3)))

    res.append("-")
    res.append("-")

    TABLE.append(res)


def second_derivative_formula(y):
    global TABLE

    res = ["-"]
    for i in range(1, len(y) - 1):
        r = y[i - 1] - 2 * y[i] + y[i + 1]
        res.append(str(round(r, 3)))
    res.append("-")

    TABLE.append(res)


def main():
    global TABLE

    interface.get_data('input.csv', TABLE, ',')

    left_formula(TABLE[1])
    centre_formula(TABLE[1])
    right_formula(TABLE[1])  # Рунге
    leveling_based_formula(TABLE[0], TABLE[1])
    second_derivative_formula(TABLE[1])

    for i in range(len(TABLE[0])):
        TABLE[0][i] = str(TABLE[0][i])
        TABLE[1][i] = str(TABLE[1][i])

    interface.print_result(TABLE)


if __name__ == "__main__":
    main()
