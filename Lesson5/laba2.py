import matplotlib.pyplot as plt
import numpy as np
t = np.array([ 1.45, 1.46, 1.50, 1.51, 1.55, 1.57, 1.58, 1.60, 1.61, 1.63])
y = np.array([ 0.429, 0.441, , 58.1, 64.2, 67.8, 69.8, 72.6, 74.2, 77.0])
x = np.array([ 30.3, 30.6, 32.9, 34.1, 35.6, 36.5, 37.0, 37.7, 38.1, 38.8])

print(y)
print(x)
u = (t**2)*x
v = y**2
print(u)
print(v)
k, b = np.polyfit(v, u, 1)
print(k)
print(b)
sigma_u = u * np.sqrt(4 * (0.01 / t)**2 + (0.0001/x)**2)
sigma_v = 2 * y * 0.0001
print(sigma_u)
print(sigma_v)

N = len(v)
mu = np.mean(u)
mv = np.mean(v)
mv2 = np.mean(v**2) 
mu2 = np.mean(u**2)
muv = np.mean (u * v)
sigma_k = np.sqrt(1/(N-2) * ( (mu2 - mu**2)/(mv2 - mv**2) - k**2 ) )
sigma_b = sigma_k * np.sqrt(mv2)
print("sigma_k = %.3f, sigma_b = %.3f" % (sigma_k, sigma_b))


fig, ax = plt.subplots(figsize=(7, 5), dpi = 300)

ax.plot(v, u, "+")
ax.set_ylabel("$u=T^2 x(ц)$,  $с^2 \cdot м$")
ax.set_xlabel("$v=y^2$, $м^2$")
ax.set_title('Рис.2. Наилучшая прямая для линеаризованной зависимости $T(y)$')
x = np.array([0., 0.7]) 
ax.plot(x, k * x + b, "g",linewidth=1, label="Линейная аппроксимация")
ax.errorbar(v, u, xerr=0.0014, yerr=0.012,color='k', linestyle='None' , label="Экспериментальные точки")
ax.legend() 

plt.savefig("laba2.png")
