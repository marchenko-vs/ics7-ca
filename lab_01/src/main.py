import sys
import interpolation as inpln


def main():

    main_table = {'x': [0.0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9, 1.05],
                  'y': [1.0, 0.838771, 0.655336, 0.450447, 0.225336, -0.01831,
                        -0.27839, -0.55243],
                  'dy': [-1.0, -1.14944, -1.29552, -1.43497, -1.56464,
                         -1.68164, -1.78333, -1.86742]}

    inpln.print_table(main_table)

    try:
        x = float(input('Введите значение аргумента, для которого'
                        ' выполняется интерполяция: '))
    except ValueError:
        print('Ошибка: аргумент должен быть вещественным числом.')
        sys.exit(1)

    try:
        n = int(input('Введите степень аппроксимирующего полинома: '))
    except ValueError:
        print('Степень должна быть целым числом.')
        sys.exit(2)

    if n < 0:
        print('Ошибка: степень должна быть неотрицательным целым числом.')
        sys.exit(3)

    if n >= len(main_table['x']):
        print('Ошибка: степень полинома должна быть меньше кол-ва'
              ' строк в таблице.')
        sys.exit(4)

    print('-----------+-----------+------------+------------')
    print('  Степень  |     x     |   Ньютон   |    Эрмит')
    print('-----------+-----------+------------+------------')

    print('{:^11d}|{:^11.6f}|{:^12.6f}|{:^12.6f}'.format(n, x,
              inpln.interpolate_newton(main_table['x'], main_table['y'], n, x),
              inpln.interpolate_hermite(main_table['x'].copy(),
                                        main_table['y'].copy(),
                                        main_table['dy'].copy(), n, x)))

    print('-----------+-----------+------------+------------')

    print('Корень функции: {:.6f}.'.format(inpln.interpolate_newton(
          main_table['y'],
          main_table['x'], n, 0.0)))


if __name__ == '__main__':
    main()
