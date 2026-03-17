import matplotlib.pyplot as plt

data = {20: 3, 28: 3, 35.5: 6, 43: 31, 51: 44, 58.5: 19, 66: 11, 74: 3}
old = [16, 24, 32, 39, 47, 55, 62, 70, 78]
m = 49.7
k = 8

keys = sorted(list(data.keys()))
counts = list(data.values())

s = sum(map(lambda x: data[x] * x, keys)) / sum(counts)
d = sum(map(lambda x: ((x - s) ** 2) * data[x], keys)) / (sum(counts) - 1) / sum(counts)
sigma = d ** .5

print(sigma)

plt.figure(figsize=(10, 6))
bars = plt.bar(range(len(keys)), counts, tick_label=keys, edgecolor='black', width=1.0)

plt.title('Гистограмма распределения')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.grid(axis='y', alpha=0.5)

for i, key in enumerate(data.keys()):
    plt.text(i, data[key] + 0.5, str(data[key]), ha='center', va='bottom')
plt.axvline(x=(m - 20) / ((old[-1] - old[0]) / k), color='red', linestyle='--', linewidth=2, label=f'Медиана = {m}')
plt.axvline(x=(s - 20) / ((old[-1] - old[0]) / k), color='green', linestyle='--', linewidth=2, label=f'Среднее значение = {round(s, 2)}')

plt.legend()
plt.tight_layout()
plt.show()

print(f"Среднее значение - {round(s, 5)}")
print(f"Медиана - {m}")
print(f"Дисперсия - {round(d, 5)}")
print(f"СКО - {round(sigma, 5)}")
