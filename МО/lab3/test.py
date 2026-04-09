import math


def f(x):
    return x ** 2 + x + math.sin(x)


def relative_error(a, b):
    if abs(b) < 1e-14:
        return abs(a - b)
    return abs((a - b) / b)


def x_bar_formula(x1, x2, x3, f1, f2, f3):
    denominator = (x2 - x3) * f1 + (x3 - x1) * f2 + (x1 - x2) * f3
    if abs(denominator) < 1e-14:
        return None

    numerator = (
        (x2**2 - x3**2) * f1
        + (x3**2 - x1**2) * f2
        + (x1**2 - x2**2) * f3
    )

    return 0.5 * numerator / denominator


def choose_new_triplet(x1, x2, x3, xb, f1, f2, f3, fb):
    points = [(x1, f1), (x2, f2), (x3, f3), (xb, fb)]
    points.sort(key=lambda p: p[0])

    filtered = []
    for x, fx in points:
        if not filtered or abs(x - filtered[-1][0]) > 1e-12:
            filtered.append((x, fx))
    points = filtered

    best_index = min(range(len(points)), key=lambda i: points[i][1])

    if 0 < best_index < len(points) - 1:
        return points[best_index - 1], points[best_index], points[best_index + 1]
    elif best_index == 0:
        return points[0], points[1], points[2]
    else:
        return points[-3], points[-2], points[-1]


def quadratic_approximation_method(x1_start, delta_x=0.25, e1=1e-4, e2=1e-4, max_iter=100):
    x1 = x1_start

    for _ in range(max_iter):
        x2 = x1 + delta_x

        f1 = f(x1)
        f2 = f(x2)

        if f1 > f2:
            x3 = x1 + 2 * delta_x
        else:
            x3 = x1 - delta_x

        f3 = f(x3)

        points = sorted([(x1, f1), (x2, f2), (x3, f3)], key=lambda p: p[0])
        (x1, f1), (x2, f2), (x3, f3) = points

        inner_count = 0
        while True:
            inner_count += 1
            if inner_count > max_iter:
                raise RuntimeError("Слишком много внутренних итераций")

            x_min, F_min = min([(x1, f1), (x2, f2), (x3, f3)], key=lambda p: p[1])

            xb = x_bar_formula(x1, x2, x3, f1, f2, f3)

            if xb is None or not math.isfinite(xb):
                x1 = x_min
                break

            fb = f(xb)

            err1 = relative_error(F_min, fb)
            err2 = relative_error(x_min, xb)

            if err1 < e1 and err2 < e2:
                return xb, fb

            if x1 <= xb <= x3:
                (p1, p2, p3) = choose_new_triplet(x1, x2, x3, xb, f1, f2, f3, fb)
                (x1, f1), (x2, f2), (x3, f3) = sorted([p1, p2, p3], key=lambda p: p[0])
            else:
                x1 = xb
                break

    raise RuntimeError("Метод не сошелся за заданное число итераций")


x_star, f_star = quadratic_approximation_method(
    x1_start=-0.5,
    delta_x=0.25,
    e1=0.0001,
    e2=0.0001
)

print("x* =", x_star)
print("f(x*) =", f_star)