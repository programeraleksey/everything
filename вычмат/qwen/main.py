import requests
import json
from google import genai

def by_local_llm(model, prompt, think):
    payload = {
        "model": model,
        "prompt": prompt,
        "think": think,
        "stream": True,
    }

    try:
        r = requests.post("http://localhost:11434/api/generate", json=payload, stream=True, timeout=600)

        if r.status_code != 200:
            print("STATUS:", r.status_code)
            print("BODY:", r.text)
            raise SystemExit

        with open("answer.txt", "w", encoding="utf-8") as f:
            for line in r.iter_lines(decode_unicode=True):
                if not line:
                    continue

                chunk = json.loads(line)
                text = chunk.get("thinking", "") + chunk.get("response", "")

                print(text, end="", flush=True)
                f.write(text)
                f.flush()

                if chunk.get("done"):
                    break
    except Exception as e:
        print("При работе программы произошла ошибка:", e)

def gemini(prompt):
    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    try:
        client = genai.Client()

        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt
        )
        text = response.text
        with open("answer.txt", "w", encoding="utf-8") as f:
            f.write(text)
            f.flush()
        print(text)
    except Exception as e:
        print("При работе программы произошла ошибка:", e)


def nonlinear_equation():
    while True:
        match input("""Выберите равенство для решения:
    1.x^3-x-2=0
    2.cos(x)-x=0
    3.e^(-x)-x=0
"""):
            case "1":
                eq = "x^3-x-2=0"
            case "2":
                eq = "cos(x)-x=0"
            case "3":
                eq = "e^(-x)-x=0"
            case _:
                print(inc_input)
                continue
        break
    while True:
        match input("""Выберите способ введения начальных данных:
1.С клавиатуры
2.Из файла
"""):
            case "1":
                stroke = input("Введите границы интервала/начальное приближение к корню и погрешность вычисления через пробел:\n").split()
            case "2":
                path = input("Введите путь к файлу. Границы интервала/начальное приближение к корню и погрешность вычисления должны быть записаны в первой строке через пробел:\n")
                with open(path, "r", encoding="utf-8") as f:
                    stroke = f.readline().split()
            case _:
                print(inc_input)
                continue
        try:
            a, b, x, e = (float(i) for i in stroke)
            if a > b:
                raise ValueError
        except ValueError:
            print(inc_input)
            continue
        break
    prompt = "Реши нелинейное уравнение " + eq
    while True:
        match input("""Выберите метод решения:
1.Метод половинного деления
2.Метод секущих
3.Метод простой итерации
"""):
            case "1":
                prompt += (f"методом половинного деления. Границы интервала [{a}, {b}], начальное приближение к корню "
                   f"x_0 = {x},  погрешность вычисления равна {e}. Проверь наличие корня на введенном интервале. Если "
                   f"на интервале несколько корней или они отсутствуют – выдай соответствующее сообщение и заверши "
                   f"работу. Проверь достаточное условие сходимости метода на введенном интервале. Выведи найденный "
                   f"корень уравнения, значение функции в корне, число итераций.")
            case "2":
                prompt += (f"методом секущих. Границы интервала [{a}, {b}],  погрешность вычисления равна {e} Проверь "
                           f"наличие корня на введенном интервале. Если на интервале несколько корней или они "
                           f"отсутствуют – выдай соответствующее сообщение и заверши работу.Выведи найденный корень "
                           f"уравнения, значение функции в корне, число итераций.")
            case "3":
                prompt += (f"методом простой итерации. Границы интервала [{a}, {b}],  погрешность вычисления равна {e} Проверь "
                           f"наличие корня на введенном интервале. Если на интервале несколько корней или они "
                           f"отсутствуют – выдай соответствующее сообщение и заверши работу.Выведи найденный корень "
                           f"уравнения, значение функции в корне, число итераций.")
            case "_":
                print(inc_input)
                continue
        break
    while True:
        match input("""Выберите модель для выполнения задания:
1.qwen3.5 (работает локально)
2.deepseek-r1 (работает локально)
3.qwen2.5 (работает локально)
4.Gemini
"""):
            case "1":
                by_local_llm("qwen3.5:latest",prompt, True )
            case "2":
                by_local_llm("deepseek-r1", prompt, True)
            case "3":
                by_local_llm("qwen2.5:7b-instruct", prompt, False)
            case "4":
                gemini(prompt)
            case _:
                print(inc_input)
                continue
        return


def nonlinear_system_equation():
    while True:
        match input("""Выберите систему для решения:
    1.x+y+3=0 & x^2+y^2-5=0
    2.x^2+y^2-1=0 & e^x+y-2=0
    3.x^2-y-1=0 & y^2-x-7=0
"""):
            case "1":
                system = "x+y+3=0 & x^2+y^2-5=0"
            case "2":
                system = "x^2+y^2-1=0 & e^x+y-2=0"
            case "3":
                system = "x^2-y-1=0 & y^2-x-7=0"
            case _:
                print(inc_input)
                continue
        break
    while True:
        stroke = input("Введите начальные приближения x_0 и y_0 через пробел:\n").split()
        if len(stroke) != 2:
            print(inc_input)
            continue
        x, y = 0, 0
        try:
            x, y = int(stroke[0]), int(stroke[1])
        except ValueError:
            print(inc_input)
            continue
        break
    prompt = f"""Реши систему нелинейных уравнений {system} с помощью метода Ньютона. Начальные приближения x_0={x} y_0={y}
Выведи вектора неизвестных: 𝑥1, 𝑥2.
Выведи количества итераций, за которое было найдено решение.
Выведи вектора  погрешностей: |x_k - x_k+1|
Проверь правильность решения системы нелинейных уравнений."""
    while True:
        match input("""Выберите модель для выполнения задания:
    1.qwen3.5 (работает локально)
    2.deepseek-r1 (работает локально)
    3.qwen2.5 (работает локально)
    4.Gemini
    """):
            case "1":
                by_local_llm("qwen3.5:latest", prompt, True)
            case "2":
                by_local_llm("deepseek-r1", prompt, True)
            case "3":
                by_local_llm("qwen2.5:7b-instruct", prompt, False)
            case "4":
                gemini(prompt)
            case _:
                print(inc_input)
                continue
        return


inc_input = "Некорректный ввод, повторите попытку"
while True:
    method = input("""Выберите тип задачи:
    1: Нелинейное уравнение        
    2: Система нелинейных уравнений
    3: Выход
""")
    match method:
        case "1":
            nonlinear_equation()
        case "2":
            nonlinear_system_equation()
        case "3":
            exit()
        case _:
            print(inc_input)
