import math

inc_input = "Некорректный ввод, повторите попытку"


def f1(x):
    return x ** 2 + 2 * x + 1


def f2(x):
    return x ** 3 - 4 * x + 2


def f3(x):
    return math.sin(x)


def f4(x):
    return math.cos(x) + x


def f5(x):
    return math.exp(x)


def tr_l(a, b, n, func):
    h = (b - a) / n
    summ = 0
    for i in range(n):
        summ += h * func(a + i * h)
    return summ


def tr_r(a, b, n, func):
    h = (b - a) / n
    summ = 0
    for i in range(n):
        summ += h * func(a + (i + 1) * h)
    return summ


def tr_m(a, b, n, func):
    h = (b - a) / n
    summ = 0
    for i in range(n):
        summ += h * func(a + i * h + h / 2)
    return summ


def trapezoid(a, b, n, func):
    h = (b - a) / n
    summ = 0
    for i in range(n):
        summ += (func(a + i * h) + func(a + (i + 1) * h)) / 2 * h
    return summ


def simpson(a, b, n, func):
    if n % 2 != 0:
        raise ValueError
    h = (b - a) / n
    summ = func(a) + func(b)
    for i in range(1, n):
        if i % 2 == 0:
            summ += 2 * func(a + i * h)
        else:
            summ += 4 * func(a + i * h)
    return summ * h / 3


def func_ch():
    while True:
        func = input("""Выберите функцию, интеграл которой требуется вычислить:
    1. x^2+2x+1     
    2. x^3-4x+2
    3. sin(x)
    4. cos(x)+x
    5. e^x
    6. Выход
    """)
        match func:
            case "1":
                f = f1
            case "2":
                f = f2
            case "3":
                f = f3
            case "4":
                f = f4
            case "5":
                f = f5
            case "6":
                exit()
            case _:
                print(inc_input)
                continue
        break
    int_limit(f)


def int_limit(func):
    while True:
        limits = input("Введите пределы интегрирования через пробел\n")
        if len(limits.split()) != 2:
            print(inc_input)
            continue
        try:
            a, b = (float(x) for x in limits.split())
        except Exception:
            print(inc_input)
            continue
        break
    accuracy(func, a, b)


def accuracy(func, a, b):
    while True:
        try:
            e = float(input("Введите Точность вычисления\n"))
            if e <= 0: raise ValueError
        except ValueError:
            print(inc_input)
            continue
        break
    int_count(func, a, b, e)


def int_count(func, a, b, e):
    while True:
        n = input("Введите значение числа разбиения интервала интегрирования (базовое значение n=4)\n")
        if n == "":
            n = 4
            break
        try:
            n = int(n)
            if n <= 0: raise ValueError
        except ValueError:
            print(inc_input)
            continue
        break
    method_ch(func, a, b, e, n)


def method_ch(func, a, b, e, n):
    while True:
        inp = input("""Выберите метод:
    1. Метод прямоугольников (левый)
    2. Метод прямоугольников (правый)
    3. Метод прямоугольников (средний)
    4. Метод трапеций
    5. Метод Симпсона
    6. Выход
    """)
        match inp:
            case "1":
                method = tr_l
                p = 1
            case "2":
                method = tr_r
                p = 1
            case "3":
                method = tr_m
                p = 2
            case "4":
                method = trapezoid
                p = 2
            case "5":
                if n % 2 != 0:
                    n += 1
                method = simpson
                p = 4
            case "6":
                exit()
            case _:
                print(inc_input)
                continue
        break
    method_manager(func, a, b, e, n, method, p)


def method_manager(func, a, b, e, n, method, p):
    i1 = method(a, b, n, func)
    while True:
        n *= 2
        i2 = method(a, b, n, func)
        r = abs(i2 - i1) / (2 ** p - 1)
        if r < e:
            print(f"Для достижения требуемой точности понадобилось разбиение на n={n} отрезков.")
            print(f"Значение вычесленного интеграла равно {i2}")
            return
        i1 = i2


def main():
    while True:
        func_ch()


if __name__ == "__main__":
    main()