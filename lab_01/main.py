from interpolation import *


def main():
    main_table = {'x': [0.0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9, 1.05],
                  'y': [1.0, 0.838771, 0.655336, 0.450447, 0.225336, -0.01831,
                        -0.27839, -0.55243],
                  'dy': [-1.0, -1.14944, -1.29552, -1.43497, -1.56464,
                         -1.68164, -1.78333, -1.86742]}
    x = 0.525
    print('-----------+-----------+-----------+-----------')
    print('     n     |     x     |   Newton  |  Hermite')
    print('-----------+-----------+-----------+-----------')
    for i in range(1, 6):
        print('{:^11d}|{:^11.6f}|{:^11.6f}|{:^11.6f}'.format(i, x,
              interpolate_newton(main_table['x'], main_table['y'], i, x),
              interpolate_hermite(main_table['x'].copy(), main_table['y'].copy(),
                                  main_table['dy'].copy(), i, x)))
        print('-----------+-----------+-----------+-----------')
    print('Function root is {:.6f}.'.format(interpolate_newton(main_table['y'],
          main_table['x'], 2, 0)))


if __name__ == '__main__':
    main()
