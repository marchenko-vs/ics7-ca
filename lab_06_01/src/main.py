import maths


def main():
    n_x = 12
    n_y = 53

    y_array, f_y_array = maths.find_solution(n_x, n_y)
    f_y = lambda x: maths.lambda_function(x, y_array, f_y_array)
    integral = maths.simpson_method(f_y, -1, 1, n_y)

    print('Значение двукратного интеграла = {:.6f}.'.format(integral))


if __name__ == '__main__':
    main()
