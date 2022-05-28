def get_data(filename: str, table: list, separator: str=' '):
    table.append([])
    table.append([])

    with open(filename, 'r') as f:
        buffer = f.readline()

        while buffer != '':
            array = buffer.strip().split(separator)
            table[0].append(int(array[0]))
            table[1].append(float(array[1]))

            buffer = f.readline()


def process_table(table: list):
    for i in range(len(table[0])):
        table[0][i] = str(table[0][i])
        table[1][i] = str(table[1][i])


def print_result(table: list):
    print('Таблица')

    print("+-----+-------+-------+-------+-------+-------+-------+")
    print("|  x  |   y   |   1   |   2   |   3   |   4   |   5   |")
    print("+-----+-------+-------+-------+-------+-------+-------+")

    for i in range(len(table[0])):
        print("|{:^5s}|{:^7s}|{:^7s}|{:^7s}|{:^7s}|{:^7s}|{:^7s}|".format(table[0][i], table[1][i],
                                                                          table[2][i], table[3][i],
                                                                          table[4][i], table[5][i],
                                                                          table[6][i]))
        print("+-----+-------+-------+-------+-------+-------+-------+")
