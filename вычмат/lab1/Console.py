from Matrix import Matrix


def matrix_interaction(matrix):
    print("Матрица успешно создана")
    matrix.calculate()
    while True:
        action = input("""Выберите действие:
    0.Сравнить результат с готовыми библиотеками
    1.Вывести определитель
    2.Вывести треугольную матрицу
    3.Вывести вектор неизвестных
    4.Вывести вектор невязок
    5.Ввести новую матрицу
    6.Завершить программу
""")
        try:
            action = int(action)
        except ValueError:
            print("Некорректный ввод, повторите попытку")
            continue
        match action:
            case 0:
                print(matrix.compare())
            case 1:
                print(matrix.det)
            case 2:
                for i in matrix.triangle_matrix:
                    print(i)
            case 3:
                if abs(matrix.det) < 1e-12:
                    print("Матрица вырождена и не имеет единтвенного решения")
                    continue
                print(matrix.answer)
            case 4:
                if abs(matrix.det) < 1e-12:
                    print("Матрица вырождена и не имеет единтвенного решения")
                    continue
                print(matrix.residual)
            case 5:
                break
            case 6:
                exit()
            case _:
                print("Некорректный ввод, повторите попытку")


def from_console():
    while True:
        n = input("Введите размерность матрицы: (n<=20)\n")
        try:
            n = int(n)
        except ValueError:
            print("Некорректный ввод, повторите попытку")
            continue
        if not (1 <= n <= 20):
            print("Размерность должны быть <=20, повторите попытку")
            continue
        break
    matrix = Matrix(n)
    print("""Введите СЛАУ в виде расширеной матрицы:
    Пример правильного ввода:
    1 2 3
    4 5 6""")
    for _ in range(n):
        while True:
            row = input().split()
            try:
                row = [float(i) for i in row]
            except ValueError:
                print("Некорректный ввод, повторите попытку")
                continue
            if len(row) == n + 1:
                matrix.append(row)
                break
            print("Некорректный ввод, повторите попытку")
    matrix_interaction(matrix)


def from_file():
    path = input("""Введите путь к файлу
Формат файла - размерность в первой строке, далее СЛАУ в виде расширеной матрицы
Размерность должны быть <=20
""")
    try:
        with open(path, "r", encoding="utf-8") as f:
            file = f.read().splitlines()
    except FileNotFoundError:
        print("Файл не найден, повторите попытку")
        return
    n = 0
    try:
        n = int(file[0])
    except ValueError:
        print("Некорретные параметры в файле")
        return
    if not (1 <= n <= 20):
        print("Размерность должны быть <=20, повторите попытку")
        return
    matrix = Matrix(n)
    if len(file) != n + 1:
        print("Некорретные параметры в файле")
        return
    for i in file[1:]:
        row = []
        try:
            row = [float(x) for x in i.split()]
        except ValueError:
            print("Некорретные параметры в файле")
            return
        if len(row) == n + 1:
            matrix.append(row)
            continue
        print("Некорретные параметры в файле")
        return
    matrix_interaction(matrix)


def main():
    while True:
        method = input("""Выберите способ введения СЛАУ:
    1.Через консоль
    2.Из файла
""")
        match method:
            case "1":
                from_console()
            case "2":
                from_file()
            case _:
                print("Некорректный ввод, повторите попытку")


if __name__ == "__main__":
    main()
