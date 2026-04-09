import csv
import matplotlib.pyplot as plt
import math
from scipy.stats import norm


x1 = []
x2 = []
x3 = []
x4 = []

with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        x1.append(float(row[0]))
        x2.append(float(row[1]))
        x3.append(float(row[2]))
        x4.append(float(row[3]))
x1.sort()
x2.sort()
x3.sort()
x4.sort()

sp = [x1, x2, x3]

# #4.1.2 Построение эмпирических функций
for i in range(3):
    plt.figure()
    plt.title(f"График имперической функции распределния F(x{i + 1})")
    plt.xlabel("x")
    plt.ylabel("F(x)")
    n = len(sp[i])
    y = [(i + 1) / n for i in range(n)]
    plt.step(sp[i], y, where='post', label=f"X{i+1}")
    plt.grid()
    plt.legend()
    plt.show()

# 4.1.4 выборочное среднее, дисперсии, стандартные отклонения, медиана, квантили
x_sr_1 = sum(x1) / len(x1)
disp_sm1 = sum([(x - x_sr_1) ** 2 for x in x1]) / len(x1)
disp1 = sum([(x - x_sr_1) ** 2 for x in x1]) / (len(x1) - 1)
s1 = math.sqrt(disp_sm1)
o1 = math.sqrt(disp1)
me1 = (x1[99] + x1[100]) / 2
q25_1 = x1[50]
q75_1 = x1[150]

x_sr_2 = sum(x2) / len(x2)
disp_sm2 = sum([(x - x_sr_2) ** 2 for x in x2]) / len(x2)
disp2 = sum([(x - x_sr_2) ** 2 for x in x2]) / (len(x2) - 1)
s2 = math.sqrt(disp_sm2)
o2 = math.sqrt(disp2)
me2 = (x2[99] + x2[100]) / 2
q25_2 = x2[50]
q75_2 = x2[150]

x_sr_3 = sum(x3) / len(x3)
disp_sm3 = sum([(x - x_sr_3) ** 2 for x in x3]) / len(x3)
disp3 = sum([(x - x_sr_3) ** 2 for x in x3]) / (len(x3) - 1)
s3 = math.sqrt(disp_sm3)
o3 = math.sqrt(disp3)
me3 = (x3[99] + x3[100]) / 2
q25_3 = x3[50]
q75_3 = x3[150]

# 4.1.3
h1_sk = 3.5 * s1 * 200 ** (-1 / 3)
k1_sk = math.ceil((x1[-1] - x1[0]) / h1_sk)
plt.figure()
plt.title("Гистограмма по X1 правилом Скотта")
plt.hist(x1, bins=k1_sk)
plt.show()

h1_fd = 2 * (q75_1 - q25_1) * 200 ** (-1 / 3)
k1_fd = math.ceil((x1[-1] - x1[0]) / h1_fd)
plt.figure()
plt.title("Гистограмма по X1 правилом Фридмана–Диакониса")
plt.hist(x1, bins=k1_fd)
plt.show()

k1_st = 1 + int(math.log(200, 2))
plt.figure()
plt.title("Гистограмма по X1 правилом Стерджеса")
plt.hist(x1, bins=k1_st)
plt.show()



h2_sk = 3.5 * s2 * 200 ** (-1 / 3)
k2_sk = math.ceil((x2[-1] - x2[0]) / h2_sk)
plt.figure()
plt.title("Гистограмма по x2 правилом Скотта")
plt.hist(x2, bins=k2_sk)
plt.show()

h2_fd = 2 * (q75_2 - q25_2) * 200 ** (-1 / 3)
k2_fd = math.ceil((x2[-1] - x2[0]) / h2_fd)
plt.figure()
plt.title("Гистограмма по x2 правилом Фридмана–Диакониса")
plt.hist(x2, bins=k2_fd)
plt.show()

k2_st = 1 + int(math.log(200, 2))
plt.figure()
plt.title("Гистограмма по x2 правилом Стерджеса")
plt.hist(x2, bins=k2_st)
plt.show()



h3_sk = 3.5 * s3 * 200 ** (-1 / 3)
k3_sk = math.ceil((x3[-1] - x3[0]) / h3_sk)
plt.figure()
plt.title("Гистограмма по x3 правилом Скотта")
plt.hist(x3, bins=k3_sk)
plt.show()

h3_fd = 2 * (q75_3 - q25_3) * 200 ** (-1 / 3)
k3_fd = math.ceil((x3[-1] - x3[0]) / h3_fd)
plt.figure()
plt.title("Гистограмма по x3 правилом Фридмана–Диакониса")
plt.hist(x3, bins=k3_fd)
plt.show()

k3_st = 1 + int(math.log(200, 2))
plt.figure()
plt.title("Гистограмма по x3 правилом Стерджеса")
plt.hist(x3, bins=k3_st)
plt.show()


#4.2
# Проанализировав по 3 гистограммы для каждой из выборок, можно четко заметить, что:
# выборка x1 имеет равномерное распределение
# выборка x2 имеет нормальное распределение
# выборка x3 имеет экспоненциальное распределние

#4.3
# для равномерного распределения находим a и b
# ММ: из формул E(X) и D(X) легко выводится, что
a_mm = x_sr_1 - math.sqrt(3 * disp_sm1)
b_mm = x_sr_1 + math.sqrt(3 * disp_sm1)
print(f"Параметры равномерного распределния, полученные методом моментов: a={a_mm}, b={b_mm}")

# ММП f(x; a, b) = 1/(b - a) => L=(1/(b-a))^n макс при min a и max b:
a_mmp = x1[0]  # данные отсортирваны, берем крайние элементы
b_mmp = x1[-1]
print(f"Параметры равномерного распределния, полученные методом максимального правдоподобия: a={a_mmp}, b={b_mmp}")
print(
    f"Можно заметить, что оценки для равномерного распределния достаточно близки: по параметру a дельта {abs(a_mm - a_mmp)}, по параметру b - {abs(b_mmp - b_mm)}")

# для нормального распредления:
# ММ: mu = E(X) и sigma^2 = D(x)
mu_mm = x_sr_2
sigma_mm = disp_sm2
print(f"Параметры нормального распределния, полученные методом моментов: mu={mu_mm}, sigma^2={sigma_mm}")

# ММП: при выводе получается то же самое, что и в ММ
mu_mmp = x_sr_2
sigma_mmp = disp_sm2
print(
    f"Параметры нормального распределния, полученные методом максимального правдоподобия: mu={mu_mmp}, sigma^2={sigma_mmp}")
print(f"Для нормального распределния параметры полученые ММ и ММП идентичны.")

# экспоненциальное распределние:
# ММ:
lambda_mm = 1 / s3
c_mm = x_sr_3 - s3
print(f"Параметры экспоненциального распределния, полученные методом моментов: lambda={lambda_mm}, c={c_mm}")

# ММП:
c_mmp = x3[0]
lambda_mmp = len(x3) / (sum(xi - x3[0] for xi in x3))
print(
    f"Параметры экспоненциального распределния, полученные методом макс правдоподобия: lambda={lambda_mmp}, c={c_mmp}")
print(
    f"Можно заметить, что для экс. распределния параметр с сильно различается: для параметра lambda delta = {abs(lambda_mmp - lambda_mm)}, для c delta = {abs(c_mmp - c_mm)}")


def emp(list, x0):
    return sum(1 if i > x0 else 0 for i in list) / len(list)

def rav(x0, a, b):
    if x0 < a:
        return 1.0
    elif x0 > b:
        return 0.0
    else:
        return (b - x0) / (b - a)


def normal(x0, mu, sigma):
    return 1 - norm.cdf(x0, loc=mu, scale=sigma)


def exp(x0, lam, c):
    if x0 < c:
        return 1.0
    return math.exp(-lam * (x0 - c))


# 4.4
# равномерное распределение:
p_emp_1 = emp(x1, x_sr_1 + o1)
p_par_1 = rav(x_sr_1 + o1, a_mmp, b_mmp)
print(f"Равномерное распределение. Эмп-ая оценка={p_emp_1}, пар-ая={p_par_1}")
print(f"Расхождение {abs(p_emp_1 - p_par_1)}")

# нормальное распределение:
p_emp_2 = emp(x2, x_sr_2 + o2)
p_par_2 = normal(x_sr_2 + o2, mu_mmp, math.sqrt(sigma_mmp))
print(f"Нормальное распределение. Эмп-ая оценка={p_emp_2}, пар-ая={p_par_2}")
print(f"Расхождение {abs(p_emp_2 - p_par_2)}")



# экспоненциальное распределение:
p_emp_3 = emp(x3, x_sr_3 + o3)
p_par_3 = exp(x_sr_3 + o3, lambda_mmp, c_mmp)
print(f"Экспоненциальное распределение. Эмп-ая оценка={p_emp_3}, пар-ая={p_par_3}")
print(f"Расхождение {abs(p_emp_3 - p_par_3)}")

print("Для всех можелей расхождение менее 1%, что является очень хорошим результатом")