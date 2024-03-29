from constants import *


def scan_argument() -> tuple:
    try:
        x = float(input('Введите значение X, для которого выполняется '
                        'интерполяция: '))

        return EXIT_SUCCESS, x
    except ValueError:
        print("Ошибка: введены данные некорректного типа!")

        return EXIT_FAILURE, 0


def scan_condition() -> tuple:
    try:
        print('\nВыберите вариант задания краевых условий на '
              'границах таблицы.\n'
              '1. Естественные краевые условия, когда вторые\nпроизводные '
              'сплайна равны нулю.\n2. На одной границе при X = X_0 вторая '
              'производная сплайна\nравна второй производной полинома Ньютона '
              'третьей степени,\nа на другой границе вторая производная равна '
              'нулю.\n3. На обеих границах при X = X_0 и X = X_N вторая\n'
              'производная сплайна равна второй\nпроизводной полинома Ньютона '
              'третьей степени.')

        condition = int(input('Введите число от 1 до 3: '))

        if condition < 1 or condition > 3:
            print("Ошибка: нужно ввести число от 1 до 3.")

            return EXIT_FAILURE, 0

        return EXIT_SUCCESS, condition
    except ValueError:
        print("Ошибка: введены данные некорректного типа!")

        return EXIT_FAILURE, 0


def print_table(table: list):
    print('Исходная таблица:')
    print('----------+----------')
    print('{:^10}|{:^10}'.format('x', 'y'))
    print('----------+----------')

    for i in range(len(table)):
        print("{:^10.3f}|{:^10.3f}".format(table[i][0], table[i][1]))
        print('----------+----------')
