import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(16,9))
ax = fig.add_subplot()

df =  pd.read_csv('BTC_data.csv')
df.time = df.time.str[:10]
time = np.array(list(df['time']))
price = np.array(list(df['close']))
time_50 = []
numbers = np.array([i+1 for i in range(len(price))])

for i in range(len(time)):
    if i % 50 == 0:
        time_50.append(time[i])

z = np.polyfit(numbers, price, 15)
func = np.poly1d(z)
yvals = func(numbers)
ax.plot(time, price, '--r')
ax.plot(numbers, yvals)
ax.set_xticks(time_50)
plt.xticks(rotation = 90)
plt.savefig('60.png')

