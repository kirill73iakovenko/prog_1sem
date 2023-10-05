import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure()
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(321)


Sep_Len = list(map(float, pd.read_csv('iris_data.csv')['SepalLengthCm']))
Sep_Wid = list(map(float,pd.read_csv('iris_data.csv')['SepalWidthCm']))
Pet_Len = list(map(float, pd.read_csv('iris_data.csv')['PetalLengthCm']))
Pet_Wid = list(map(float, pd.read_csv('iris_data.csv')['PetalWidthCm']))


ax1.errorbar = (Sep_Len, Sep_Wid, linestyle = 'None')
ax2.errorbar = (Pet_Len, Pet_Wid, linestyle = 'None')
ax3.errorbar = (Pet_Len, Sep_Wid, linestyle = 'None')

ax1.set_title('Sep_Wid(Sep_len)')
ax2.set_title('Pet_Wid(Pet_len)')
ax3.set_title('Set_Wid(Pet_len)')
'''ax4.set_title('Pet_Wid(Sep_Len)')
ax5.set_title('Pet_Len(Set_Len)')
ax6.set_title('Pet_Wid(Set_Wid)')'''

plt.savefig('4.png', dpi = 300)
