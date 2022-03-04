import sys
import interpolation as inpln


def main():
    try:
        x = float(input('Введите аргумент функции: '))
        n = int(input('Введите степень полинома: '))
    except ValueError:
        print('Аргумент должен быть вещественным числом.')
        sys.exit(1)

    main_table = {'x': [0.0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9, 1.05],
                  'y': [1.0, 0.838771, 0.655336, 0.450447, 0.225336, -0.01831,
                        -0.27839, -0.55243],
                  'dy': [-1.0, -1.14944, -1.29552, -1.43497, -1.56464,
                         -1.68164, -1.78333, -1.86742]}

    inpln.print_table(main_table)

    print('-----------+-----------+-----------+-----------')
    print('     n     |     x     |   Newton  |  Hermite')
    print('-----------+-----------+-----------+-----------')

    for i in range(1, n + 1):
        print('{:^11d}|{:^11.6f}|{:^11.6f}|{:^11.6f}'.format(i, x,
              inpln.interpolate_newton(main_table['x'], main_table['y'], i, x),
              inpln.interpolate_hermite(main_table['x'].copy(), 
                                        main_table['y'].copy(),
                                        main_table['dy'].copy(), i, x)))
        print('-----------+-----------+-----------+-----------')

    print('Корень функции: {:.6f}.'.format(inpln.interpolate_newton(
          main_table['y'],
          main_table['x'], n, 0.0)))


if __name__ == '__main__':
    main()
