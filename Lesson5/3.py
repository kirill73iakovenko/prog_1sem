import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

flowers = list(pd.read_csv('iris_data.csv')['Species'])
names = []
amount = []

for i in range(len(flowers)):
    if flowers[i] not in names:
        amount.append(flowers.count(flowers[i]))
        names.append(flowers[i])
        

length = list(pd.read_csv('Iris_data.csv')['PetalLengthCm'])
length1, length2, length3 = 0, 0, 0
for i in range(len(length)):
    if length[i] < 1.2:
        length1 += 1
    elif 1.2 <= length[i] <= 1.5:
        length2 += 1
    else:
        length3 += 1
fig, (ax1, ax2) = plt.subplots(2, dpi = 300)
ax1.pie([amount[i] for i in range(len(amount))], labels = [names[i] for i in range(len(names))])
ax1.set_title(' Proportion of species', color = 'r')
ax2.pie([length1, length2, length3], labels = [ 'length <1.2 см' , ' 1.2 <= length <= 1.5', 'length > 1.5'])
ax2.set_title('Length', color = 'b')
plt.savefig("species.png")
