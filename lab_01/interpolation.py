EPS = 1e-3


def print_table(table: dict):
    print('Исходная таблица:')

    print('-----------+-----------+------------')
    print('     x     |     y     |     dy     ')
    print('-----------+-----------+------------')

    for i in range(len(table['x'])):
        print('{:^11.6f}|{:^11.6f}|{:^11.6f}'.format(table['x'][i],
                                                     table['y'][i],
                                                     table['dy'][i]))
        print('-----------+-----------+------------')


def divided_difference_newton(x: list, y: list) -> float:
    if len(x) == 2:
        return (y[1] - y[0]) / (x[1] - x[0])
    return (divided_difference_newton(x[:len(x) - 1], y[:len(x) - 1]) -
            divided_difference_newton(x[1:], y[1:])) / (x[0] - x[len(x) - 1])


def interpolate_newton(x: list, y: list, degree: int, argument: float) -> float:
    function = y[0]
    for i in range(1, degree + 2):
        multiplier = 1.0
        for j in range(0, i):
            multiplier *= argument - x[j]
        multiplier *= divided_difference_newton(x[:i + 1], y[:i + 1])
        function += multiplier
    return function


def divided_difference_hermite(x: list, y: list, dy: list) -> float:
    if len(x) == 2:
        if abs(x[1] - x[0]) > EPS:
            return (y[1] - y[0]) / (x[1] - x[0])
        return dy[0]
    return (divided_difference_hermite(x[:len(x) - 1], y[:len(x) - 1],
                                       dy[:len(x) - 1]) -
            divided_difference_hermite(x[1:], y[1:], dy[1:])) / (
                       x[0] - x[len(x) - 1])


def interpolate_hermite(x: list, y: list, dy: list, degree: int,
                        argument: float) -> float:
    length = len(x)
    for i in range(0, length, 2):
        x.insert(i + 1, x[i])
        y.insert(i + 1, y[i])
        dy.insert(i + 1, dy[i])
    function = y[0]
    for i in range(1, degree + 2):
        multiplier = 1.0
        for j in range(0, i):
            multiplier *= argument - x[j]
        multiplier *= divided_difference_hermite(x[:i + 1], y[:i + 1],
                                                 dy[:i + 1])
        function += multiplier
    return function
