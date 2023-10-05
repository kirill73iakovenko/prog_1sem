import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fib = plt.figure()
ax = fib.add_subplot()

PetLen = list(map(float, pd.read_csv('iris_data.csv')['PetalLengthCm']))
PetWid = list(map(float, pd.read_csv('iris_data.csv')['PetalWidthCm']))

k, b = np.polyfit(PetLen, PetWid, 1)

fig, ax = plt.subplots()
x = np.array([1., 7.2])
ax.plot(x, k * x + b, "-r",linewidth=1, label = 'Линейная аппроксимация')
ax.errorbar(PetLen, PetWid, yerr = 0.01, xerr = 0.001, color = 'b', linestyle = 'None', label = 'Экспериментальные точки')
ax.set_xlabel("Длина лепестка, см")
ax.set_ylabel("Ширина лепестка, см")
ax.set_title("Зависимость ширины лепестков от их длины")
ax.legend()
plt.savefig('4(3).png')
