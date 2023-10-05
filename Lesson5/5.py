import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(16,9))
ax = fig.add_subplot()

df =  pd.read_csv('BTC_data.csv')
df.time = df.time.str[:10]
time = list(df['time'])
price = list(df['close'])
time_50 = []
for i in range(len(time)):
    if i % 50 == 0:
        time_50.append(time[i])
ax.plot(time, price)
ax.set_xticks(time_50)
plt.xticks(rotation = 90)
plt.savefig('5.png')

