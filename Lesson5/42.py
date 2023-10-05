import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fib = plt.figure(figsize = (9, 16))
ax1 = fib.add_subplot(311)
ax2 = fib.add_subplot(312)
ax3 = fib.add_subplot(313)

SepLen = list(map(float, pd.read_csv('iris_data.csv')['SepalLengthCm']))
SepWid = list(map(float,pd.read_csv('iris_data.csv')['SepalWidthCm']))
PetLen = list(map(float, pd.read_csv('iris_data.csv')['PetalLengthCm']))
PetWid = list(map(float, pd.read_csv('iris_data.csv')['PetalWidthCm']))

ax1.errorbar(SepLen, SepWid, yerr = 0.1, xerr = 0.01, color = 'r', linestyle = 'None')
ax2.errorbar(PetLen, PetWid, yerr = 0.1, xerr = 0.01, color = 'g', linestyle = 'None')
ax3.errorbar(PetLen, SepLen, yerr = 0.1, xerr = 0.01, color = '0', linestyle = 'None')
ax1.set_title('SepWid(SepLen)')
ax2.set_title('PetWid(PetLen)')
ax3.set_title('SepLen(PetLen)')
plt.savefig('4(1).png', dpi = 300)

ger = plt.figure(figsize = (9, 16))
ax1 = ger.add_subplot(311)
ax2 = ger.add_subplot(312)
ax3 = ger.add_subplot(313)
SepLen = list(map(float, pd.read_csv('iris_data.csv')['SepalLengthCm']))
SepWid = list(map(float,pd.read_csv('iris_data.csv')['SepalWidthCm']))
PetLen = list(map(float, pd.read_csv('iris_data.csv')['PetalLengthCm']))
PetWid = list(map(float, pd.read_csv('iris_data.csv')['PetalWidthCm']))

ax1.errorbar(PetWid, SepWid, yerr = 0.1, xerr = 0.01, color = 'm', linestyle = 'None')
ax2.errorbar(PetLen, SepWid, yerr = 0.1, xerr = 0.01, color = 'y', linestyle = 'None')
ax3.errorbar(SepLen, PetWid, yerr = 0.1, xerr = 0.01, color = 'c', linestyle = 'None')
ax1.set_title('SepWid(PetWid)')
ax2.set_title('SepWid(PetLen)')
ax3.set_title('PetWid(SepLen)')
plt.savefig('4(2).png', dpi = 300)



