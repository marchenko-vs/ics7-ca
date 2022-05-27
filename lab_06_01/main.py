import maths


def main():
    ny = 55
    nx = 10
    y_arr, fy_arr = maths.solution(ny, nx)

    fy = lambda x: maths.f(x, y_arr, fy_arr)
    res = maths.simpson(fy, -1, 1, ny)
    print(res)


if __name__ == '__main__':
    main()
