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


def f6(x):
    return 1 / x


def f7(x):
    return 1 / math.sqrt(x)


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
    6. 1/x
    7. 1/sqrt(x)
    8. Выход
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
                f = f6
            case "7":
                f = f7
            case "8":
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
            if b - a <= 0:
                raise ValueError
        except ValueError:
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
            if n <= 0 or n % 2 != 0: raise ValueError
        except ValueError:
            print(inc_input)
            continue
        break
    method_ch(func, a, b, e, n)


def method_ch(func, a, b, e, n):
    if func == f6 and a <= 0 <= b:
        print("Интеграл не существует")
        return
    elif func == f7 and a <= 0:
        if a < 0:
            print(inc_input)
            return
        delta = 0.1
        method = [tr_l, tr_r, tr_m, trapezoid, simpson]
        p = [1, 1, 2, 2, 4]
        count = 0
        for _ in range(70):
            _, i1 = method_manager(func, delta, b, e, n, method[count], p[count])
            delta /= 2
            _, i2 = method_manager(func, delta, b, e, n, method[count], p[count])
            if abs(i2 - i1) < e:
                match count:
                    case 0:
                        print("1. Решение Методом прямоугольников (левый)")
                        print(f"Значение вычесленного интеграла равно {i2}")
                    case 1:
                        print("2. Решение Методом прямоугольников (правый)")
                        print(f"Значение вычесленного интеграла равно {i2}")
                    case 2:
                        print("3. Решение Методом прямоугольников (средний)")
                        print(f"Значение вычесленного интеграла равно {i2}")
                    case 3:
                        print("4. Решение Методом трапеций")
                        print(f"Значение вычесленного интеграла равно {i2}")
                    case 4:
                        print("5. Решение Методом Симпсона")
                        print(f"Значение вычесленного интеграла равно {i2}")
                        return
                delta = 0.1
                count += 1
        print("Не удалось установить сходимость")
        return

    print("1. Решение Методом прямоугольников (левый)")
    x, y = method_manager(func, a, b, e, n, tr_l, 1)
    print(f"Для достижения требуемой точности понадобилось разбиение на n={x} отрезков.")
    print(f"Значение вычесленного интеграла равно {y}")
    print("2. Решение Методом прямоугольников (правый)")
    x, y = method_manager(func, a, b, e, n, tr_r, 1)
    print(f"Для достижения требуемой точности понадобилось разбиение на n={x} отрезков.")
    print(f"Значение вычесленного интеграла равно {y}")
    print("3. Решение Методом прямоугольников (средний)")
    x, y = method_manager(func, a, b, e, n, tr_m, 2)
    print(f"Для достижения требуемой точности понадобилось разбиение на n={x} отрезков.")
    print(f"Значение вычесленного интеграла равно {y}")
    print("4. Решение Методом трапеций")
    x, y = method_manager(func, a, b, e, n, trapezoid, 2)
    print(f"Для достижения требуемой точности понадобилось разбиение на n={x} отрезков.")
    print(f"Значение вычесленного интеграла равно {y}")
    print("5. Решение Методом Симпсона")
    x, y = method_manager(func, a, b, e, n, simpson, 4)
    print(f"Для достижения требуемой точности понадобилось разбиение на n={x} отрезков.")
    print(f"Значение вычесленного интеграла равно {y}")
    return


def method_manager(func, a, b, e, n, method, p):
    i1 = method(a, b, n, func)
    while True:
        n *= 2
        i2 = method(a, b, n, func)
        r = abs(i2 - i1) / (2 ** p - 1)
        if r < e:
            return n, i2
        i1 = i2


def main():
    while True:
        func_ch()


if __name__ == "__main__":
    main()
