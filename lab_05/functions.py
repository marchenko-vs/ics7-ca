from constants import *
from matplotlib import pyplot as plt


def initial_functions(k, alpha, p, f, i, T, a0, R):
    k[i] = A_1 * (B_1 + C_1 * (T[i] ** M_1))
    alpha[i] = a0 * (T[i] / DELTA - 1) ** 4 + GAMMA
    p[i] = 2 / R * alpha[i]
    f[i] = 2 * T_0 / R * alpha[i]


def left_border_coefficients(k, A, B, C, D, A_, B_, C_, D_, T, f, p, F0, a0, h, i=0):
    """находим коэффициенты при левом краевом условии"""
    k[i + 1] = A_1 * (B_1 + C_1 * (T[i + 1] ** M_1))
    A[i] = 0
    B[i] = (k[i] + k[i + 1]) / 2 + p[i] * h ** 2
    C[i] = (k[i] + k[i + 1]) / 2
    D[i] = f[i] * h ** 2 + F0 * h
    A_[i] = 0
    B_[i] = B[i] + (A_1 * C_1 * M_1 / 2 * (T[i] ** (M_1 - 1)) + 8 * a0 / (DELTA * R) * (
            T[i] / DELTA - 1) ** 3 * h ** 2) * T[i] - (A_1 * C_1 * M_1 / 2 * (T[i] ** (M_1 - 1))) * T[
                i + 1] - (
                    8 * T_0 * a0 / (DELTA * R) * (T[i] / DELTA - 1) ** 3 * h ** 2)
    C_[i] = -(A_1 * C_1 * M_1 / 2 * (T[i + 1] ** (M_1 - 1))) * T[i] + (A_1 * C_1 * M_1 / 2 * (
            T[i + 1] ** (M_1 - 1))) * T[i + 1] + C[i]
    D_[i] = - B[i] * T[i] + C[i] * T[i + 1] + D[i]


def right_border_coefficients(k, A, B, C, D, A_, B_, C_, D_, T, f, p, a, a0, h, i):
    """находим коэффициенты при правом краевом условии"""
    A[i] = (k[i - 1] + k[i]) / 2
    B[i] = (k[i - 1] + k[i]) / 2 + p[i] * h ** 2 + a[i] * h
    C[i] = 0
    D[i] = f[i] * h ** 2 + a[i] * T_0 * h
    A_[i] = (A_1 * C_1 / 2 * M_1 * (T[i - 1] ** (M_1 - 1))) * T[i - 1] + A[i] - (A_1 * C_1 / 2 * M_1 * (
            T[i - 1] ** (M_1 - 1))) * T[i]
    B_[i] = -A_1 * C_1 * M_1 / 2 * (T[i] ** (M_1 - 1)) * T[i - 1] + B[i] + (
            A_1 * C_1 * M_1 / 2 * (T[i] ** (M_1 - 1)) + 8 * a0 / (DELTA * R) * (
            T[i] / DELTA - 1) ** 3 * h ** 2 + 4 * a0 / DELTA * (T[i] / DELTA - 1) ** 3 * h) * T[i] - (
                    8 * T_0 * a0 / (DELTA * R) * (T[i] / DELTA - 1) ** 3 * h ** 2 + 4 * a0 / DELTA * (
                    T[i] / DELTA - 1) ** 3 * T_0 * h)
    C_[i] = 0
    D_[i] = A[i] * T[i - 1] - B[i] * T[i] + D[i]


def non_border_coefficients(k, A, B, C, D, A_, B_, C_, D_, T, f, p, a0, h, i):
    """находим коэффициенты"""
    k[i + 1] = A_1 * (B_1 + C_1 * (T[i + 1] ** M_1))
    A[i] = (k[i - 1] + k[i]) / 2
    B[i] = (k[i - 1] + k[i]) / 2 + (k[i] + k[i + 1]) / 2 + p[i] * h ** 2
    C[i] = (k[i] + k[i + 1]) / 2
    D[i] = f[i] * h ** 2
    A_[i] = (A_1 * C_1 / 2 * M_1 * (T[i - 1] ** (M_1 - 1))) * T[i - 1] + A[i] - (
            A_1 * C_1 / 2 * M_1 * (T[i - 1] ** (M_1 - 1))) * T[i]
    B_[i] = -A_1 * C_1 * M_1 / 2 * (T[i] ** (M_1 - 1)) * T[i - 1] + B[i] + (
            A_1 * C_1 * M_1 * (T[i] ** (M_1 - 1)) + 8 * a0 / (DELTA * R) * (
            T[i] / DELTA - 1) ** 3 * h ** 2) * T[i] - (
                    A_1 * C_1 * M_1 / 2 * (T[i] ** (M_1 - 1)) * T[i + 1]) - (
                    8 * T_0 * a0 / (DELTA * R) * (T[i] / DELTA - 1) ** 3 * h ** 2)
    C_[i] = -(A_1 * C_1 * M_1 / 2 * (T[i + 1] ** (M_1 - 1))) * T[i] + (
            A_1 * C_1 * M_1 / 2 * (T[i + 1] ** (M_1 - 1))) * T[i + 1] + C[i]
    D_[i] = A[i] * T[i - 1] - B[i] * T[i] + C[i] * T[i + 1] + D[i]


def sweep_coefficients(ksi, eta, A, B, C, D, i):
    """прогоночные коэффициенты, изначальные кси и эта равны нулю"""
    ksi[i] = C[i - 1] / (B[i - 1] - A[i - 1] * ksi[i - 1])
    eta[i] = (A[i - 1] * eta[i - 1] + D[i - 1]) / (B[i - 1] - A[i - 1] * ksi[i - 1])


def reverse_course(ksi, eta, N, dy, T, A_, B_, D_):
    """обратный ход - вычисляем дельта y - расстояние между точками в сетке"""
    max_dy = 0

    for i in range(N, -1, -1):
        if i < N:
            dy[i] = ksi[i + 1] * dy[i + 1] + eta[i + 1]
        else:
            dy[i] = (A_[i] * eta[i] + D_[i]) / (B_[i] - A_[i] * ksi[i])
        max_dy = max(max_dy, abs(dy[i] / T[i]))

    return max_dy


def show(N, h, a0, F0, T):
    x = [0 for j in range(N + 1)]

    for i in range(1, N + 1):
        x[i] = x[i - 1] + h

    fig, ax = plt.subplots()
    text = "N=" + str(N) + ", F0=" + str(F0) + ", a0=" + str(a0) + ", EPS=" + str(EPS)
    plt.title(text)
    ax.plot(x, T, '-')
    ax.set_xlabel('Расстояние от левого торца стержня, см')
    ax.set_ylabel('Температура, К')
    ax.grid(True)
    plt.show()
