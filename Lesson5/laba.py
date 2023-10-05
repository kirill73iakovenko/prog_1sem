import matplotlib.pyplot as plt
y = [21.3, 42.9, 44.1, 53.3, 58.1, 64.2, 67.8, 69.8, 72.6, 74.2, 77.0]
t = [1.43, 1.45, 1.46, 1.50, 1.51, 1.55, 1.57, 1.58, 1.60, 1.61, 1.63]

plt.ylabel("$T$, c")
plt.xlabel("$y$, см")
plt.title('Рис.1. График зависимости периода $T$ от положения призмы $y$')
plt.grid(True, linestyle="--")
plt.errorbar(y, t, xerr= 0.1, yerr= 0.01, fmt=".k", label="Экспериментальные точки")
plt.plot(y, t, "--r", linewidth=1, label="Кусочно линейная интерполяция")
plt.plot([0.00,80.0], [1.43, 1.43], "--b", linewidth=1, label="Минимум")
plt.legend()
plt.savefig('laba.png')
