import numpy as np
import matplotlib.pyplot as plt

values1 = np.random.normal(0, 10, 1000)
plt.hist(values1, 100, color = "green", alpha = 0.5, density = True)

values2 = np.random.normal(0, 10, 10000000)
plt.hist(values2, 100, color = "red", alpha = 0.5, density = True)


plt.savefig("52.png")


