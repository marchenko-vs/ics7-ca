import functions as funcs

from constants import *


def main():
    while True:
        l = 10
        F_0 = 50
        alpha_0 = 1.94 * 10 ** (-2)
        N = 100

        print("1. Тест 1 - F_0 = 50 (подача тепла).\n"
              "2. Тест 2 - F_0 = -10 (отвод тепла).\n"
              "3. Тест 3 - alpha_0 = 3 * alpha_0 (ускорение подачи тепла).\n"
              "4. Тест 4 - F_0 = 0 (температура стержня не меняется).\n"
              "5. Пользовательские параметры.\n"
              "0. Выход.")

        test = input("Введите пункт меню: ")

        match test:
            case '0':
                print("Выход.")
                return
            case '1':
                F_0 = 50
            case '2':
                F_0 = -10
            case '3':
                alpha_0 *= 3
            case '4':
                F_0 = 0
            case '5':
                F_0 = float(input("Введите F_0: "))
                N = int(input("Введите число точек: "))
                coefficients = float(input("Коэффициент, на который умножить alpha_0 (alpha_0 = 0.0194): "))
                alpha_0 *= coefficients
            case _:
                print("Ошибка: пункт меню должен быть цифрой от 0 до 5.")
                continue

        h = l / N

        T = [T_0 for i in range(N + 1)]
        k = [0 for i in range(N + 1)]
        p = [0 for i in range(N + 1)]

        A = [0 for i in range(N + 1)]
        B = [0 for i in range(N + 1)]
        C = [0 for i in range(N + 1)]
        D = [0 for i in range(N + 1)]

        a = [0 for i in range(N + 1)]
        f = [0 for i in range(N + 1)]

        A_ = [0 for i in range(N + 1)]
        B_ = [0 for i in range(N + 1)]
        C_ = [0 for i in range(N + 1)]
        D_ = [0 for i in range(N + 1)]

        ksi = [0 for i in range(N + 1)]
        eta = [0 for i in range(N + 1)]
        dy = [0 for i in range(N + 1)]

        j = 0

        while j < MAX_ITERATIONS:
            for i in range(N + 1):

                funcs.initial_functions(k, a, p, f, i, T, alpha_0, R)  # задаем значения функций

                # получаем коэффициенты СЛАУ с трехдиагональной матрицей
                if i == 0:
                    funcs.left_border_coefficients(k, A, B, C, D, A_, B_, C_, D_, T, f, p, F_0, alpha_0, h)
                elif i == N:
                    funcs.right_border_coefficients(k, A, B, C, D, A_, B_, C_, D_, T, f, p, a, alpha_0, h, N)
                else:
                    funcs.non_border_coefficients(k, A, B, C, D, A_, B_, C_, D_, T, f, p, alpha_0, h, i)

                # прямой ход - находим кси и ета для метода Гаусса
                if i > 0:
                    funcs.sweep_coefficients(ksi, eta, A_, B_, C_, D_, i)

            # максимальная разность между значением и узлом
            max_dy = funcs.reverse_course(ksi, eta, N, dy, T, A_, B_, D_)

            if max_dy < EPS:
                break
            else:
                for i in range(N + 1):
                    T[i] += dy[i]

            j += 1

        funcs.show(N, h, alpha_0, F_0, T)


if __name__ == "__main__":
    main()
