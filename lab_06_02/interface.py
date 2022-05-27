def print_table(table):
    print("|  x  |   y   |   1   |   2   |   3   |   4   |   5   |")
    print("-------------------------------------------------------")

    for i in range(len(table[0])):
        print("|%5s|%7s|%7s|%7s|%7s|%7s|%7s|" % (table[0][i], table[1][i],
                                                 table[2][i], table[3][i],
                                                 table[4][i], table[5][i],
                                                 table[6][i]))
