class Point:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0, weight: float = 1):
        self.x = x
        self.y = y
        self.z = z
        self.weight = weight

    def __str__(self) -> str:
        return f"|{self.x:^10.2f} | {self.y:^10.2f} | {self.z:^10.2f} | {self.weight:^10.2f} |"


def find_linear_system_matrix(dots: list, n: int) -> list:
    global coefficient

    rn = 0
    for i in range(0, n + 1):
        rn += i + 1
    res = [[0 for i in range(0, rn)] for j in range(0, rn)]
    col = [0 for i in range(0, rn)]
    v = 0
    for i in range(0, n + 1):
        for j in range(0, i + 1):
            for h in range(len(dots)):
                c = 0
                for k in range(0, n + 1):
                    for l in range(0, k + 1):
                        coefficient = dots[h].weight * dots[h].x ** (i - j) * dots[h].y ** j
                        res[v][c] += coefficient * dots[h].x ** (k - l) * dots[h].y ** l
                        c += 1
                col[v] += coefficient * dots[h].z
            v += 1

    for i in range(len(col)):
        res[i].append(col[i])

    return res


def gaussian_elimination(matrix: list) -> list:
    n = len(matrix)

    for k in range(n):
        for i in range(k + 1, n):
            coefficient = -(matrix[i][k] / matrix[k][k])

            for j in range(k, n + 1):
                matrix[i][j] += coefficient * matrix[k][j]

    a = [0 for i in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            matrix[i][n] -= a[j] * matrix[i][j]

        a[i] = matrix[i][n] / matrix[i][i]

    return a


def get_polynomial_coefficients(matrix: list) -> list:
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                continue

            multiplication = matrix[j][i] / matrix[i][i]

            for k in range(0, len(matrix) + 1):
                matrix[j][k] -= multiplication * matrix[i][k]

    for i in range(len(matrix)):
        multiplication = matrix[i][i]

        for j in range(len(matrix[i])):
            matrix[i][j] /= multiplication

    return [matrix[i][-1] for i in range(len(matrix))]
