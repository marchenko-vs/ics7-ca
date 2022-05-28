EXIT_SUCCESS = 0
EXIT_FAILURE = 1

EPS = 1e-3


def get_data(size: int) -> tuple:
    return_code = EXIT_FAILURE
    return_data = (return_code, 0, 0, 0, 0, 0, 0)

    try:
        n_x = int(input('Enter polynomial degree of N_X: '))
    except ValueError:
        print('Error: polynomial degree must be an integer.')
        return return_data

    if n_x < 0 or n_x >= size:
        print(f'Error: polynomial degree must be from 0 to {size - 1}.')
        return return_data

    try:
        n_y = int(input('Enter polynomial degree of N_Y: '))
    except ValueError:
        print('Error: polynomial degree must be an integer.')
        return return_data

    if n_y < 0 or n_y >= size:
        print(f'Error: polynomial degree must be from 0 to {size - 1}.')
        return return_data

    try:
        n_z = int(input('Enter polynomial degree of N_Z: '))
    except ValueError:
        print('Error: polynomial degree must be an integer.')
        return return_data

    if n_z < 0 or n_z >= size:
        print(f'Error: polynomial degree must be from 0 to {size - 1}.')
        return return_data

    print()

    try:
        x = float(input('Enter value of X: '))
    except ValueError:
        print(f'Error: X must be float.')
        return return_data

    try:
        y = float(input('Enter value of Y: '))
    except ValueError:
        print(f'Error: Y must be float.')
        return return_data

    try:
        z = float(input('Enter value of Z: '))
    except ValueError:
        print(f'Error: Y must be float.')
        return return_data

    print()

    return EXIT_SUCCESS, n_x, n_y, n_z, x, y, z


def get_table() -> list:
    data = list()

    z_0 = [[0, 1, 4, 9, 16],
           [1, 2, 5, 10, 17],
           [4, 5, 8, 13, 20],
           [9, 10, 13, 18, 25],
           [16, 17, 20, 25, 32]]

    z_1 = [[1, 2, 5, 10, 17],
           [2, 3, 6, 11, 18],
           [5, 6, 9, 14, 21],
           [10, 11, 14, 19, 26],
           [17, 18, 21, 26, 33]]

    z_2 = [[4, 5, 8, 13, 20],
           [5, 6, 9, 14, 21],
           [8, 9, 12, 17, 24],
           [13, 14, 17, 22, 29],
           [20, 21, 24, 29, 36]]

    z_3 = [[9, 10, 13, 18, 25],
           [10, 11, 14, 19, 26],
           [13, 14, 17, 22, 29],
           [18, 19, 22, 27, 34],
           [25, 26, 29, 34, 41]]

    z_4 = [[16, 17, 20, 25, 32],
           [17, 18, 21, 26, 33],
           [20, 21, 24, 29, 36],
           [25, 26, 29, 34, 41],
           [32, 33, 36, 41, 48]]

    data.append(z_0)
    data.append(z_1)
    data.append(z_2)
    data.append(z_3)
    data.append(z_4)

    return data


# def print_table(table: list, z: int):
#     print(f'Z = {z}')
#
#     print('---------+---------+---------+---------+----------')
#
#     for i in range(len(table[0])):
#         print('{:^9.4f}|{:^9.4f}|{:^9.4f}|{:^9.4f}|{:^9.4f}'.format(
#             table[i][0], table[i][1], table[i][2], table[i][3], table[i][4]))
#
#         print('---------+---------+---------+---------+----------')
#
#     print()


def print_table(table: list, z: int):
    length_i = len(table)
    length_j = len(table[0])

    if not z is None:
        print(f'Z = {z}')

    if length_i == 5:
        print('---------+---------+---------+---------+----------')
    else:
        print('---------+---------+----------')

    for i in range(length_i):
        for j in range(length_j):
            print('{:^9.4f}'.format(table[i][j]), end='')

            if j < len(table[0]) - 1:
                print('|', end='')
            else:
                print()

        if length_i == 5:
            print('---------+---------+---------+---------+----------')
        else:
            print('---------+---------+----------')

    print()


def print_all_tables(table: list):
    for i in range(len(table)):
        print_table(table[i], i)


def get_range(table: list, degree: int, argument: float) -> int:
    index = -1
    length = len(table)

    for element in table:
        if element[0] > argument:
            break

        index += 1

    if index <= degree // 2:
        return 0

    if index >= length - degree // 2 - 1:
        return length - degree

    if argument - table[index][0] < EPS:
        return index - degree // 2

    if argument - table[index][0] < argument - table[index + 1][0]:
        return index - degree // 2

    return index - degree // 2 + 1


def divided_difference(x_0: float, x_1: float, y_0: float, y_1: float) -> float:
    if abs(x_0 - x_1) > EPS:
        return (y_0 - y_1) / (x_0 - x_1)


def newton_interpolation(table: list, degree: int, argument: float) -> float:
    index = get_range(table, degree + 1, argument)
    result = table[index][1]

    for i in range(degree):
        for j in range(degree - i):
            table[index + j][1] = divided_difference(
                table[index + j][0], table[index + j + i + 1][0],
                table[index + j][1], table[index + j + 1][1])

        multiplier = 1

        for j in range(i + 1):
            multiplier *= (argument - table[index + j][0])

        multiplier *= table[index][1]
        result += multiplier

    return result


def double_interpolation(table: list, degree_x: int, degree_y: int,
                         argument_x: float, argument_y: float) -> float:
    length = len(table)
    array_1 = list()

    for i in range(length):
        array_tmp = []

        for j in range(length):
            array_tmp.append([j, table[i][j]])

        array_1.append(newton_interpolation(array_tmp, degree_x, argument_x))

    array_2 = list()

    for i in range(length):
        array_2.append([i, array_1[i]])

    return newton_interpolation(array_2, degree_y, argument_y)


def triple_interpolation(table: list, degree_x: int, degree_y: int,
                         degree_z: int, argument_x: float, argument_y: float,
                         argument_z: float) -> float:
    length = len(table)
    array = list()

    for i in range(length):
        array.append([i, double_interpolation(table[i], degree_x, degree_y,
                                              argument_x, argument_y)])

    return newton_interpolation(array, degree_z, argument_z)
