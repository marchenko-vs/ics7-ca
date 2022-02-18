def separate_function(x: list, y: list) -> float:
    if len(x) == 2:
        return (y[1] - y[0]) / (x[1] - x[0])
    return (separate_function(x[:len(x) - 1], y[:len(x) - 1]) -
            separate_function(x[1:], y[1:])) / (x[0] - x[len(x) - 1])


def separate_function_2(x: list, y: list, dy: list) -> float:
    if abs(x[1] - x[0]) < 1e-3:
        return dy[0]
    return separate_function(x, y)


def interpolate_hermite(x: list, y: list, dy: list, degree: int,
                        argument: float) -> float:
    function = y[0]
    for i in range(1, degree + 1):
        multiplier = 1.0
        for j in range(0, i):
            multiplier *= argument - x[j]
        multiplier *= separate_function_2(x[:i + 1], y[:i + 1], dy[:i + 1])
        function += multiplier
    return function


def interpolate_newton(x: list, y: list, degree: int, argument: float) -> float:
    function = y[0]
    for i in range(1, degree + 1):
        multiplier = 1.0
        for j in range(0, i):
            multiplier *= argument - x[j]
        multiplier *= separate_function(x[:i + 1], y[:i + 1])
        function += multiplier
    return function


def interpolate_hermite(x: list, y: list, dy: list, nodes: int,
                        argument: float) -> float:
    length = len(x)
    for i in range(0, length, 2):
        x.insert(i + 1, x[i])
        y.insert(i + 1, y[i])
        dy.insert(i + 1, dy[i])
    function = y[0]
    for i in range(1, nodes + 1):
        multiplier = 1.0
        for j in range(0, i):
            multiplier *= argument - x[j]
        multiplier *= separate_function_2(x[:i + 1], y[:i + 1], dy[:i + 1])
        function += multiplier
    return function
