import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from scipy.stats import linregress

tornadoes = pd.read_csv("tornadoes.csv")
mississippi_land_area = 48430
oklahoma_land_area = 69899
tornadoes.set_index('Year',inplace=True)
tornadoes.insert(2,"OK/square mile",[row['Oklahoma']/oklahoma_land_area for index,row in tornadoes.iterrows()],True)
tornadoes.insert(3,"MS/square mile",[row['Mississippi']/mississippi_land_area for index,row in tornadoes.iterrows()],True)
plt.figure(figsize=[16,9])
plt.plot(tornadoes['MS/square mile'],color="blue",marker='o')
plt.plot(tornadoes['OK/square mile'],color="red",marker='o')
tornadoes['OK/square mile'].rolling(window=10,min_periods=1,center=False).mean().plot(color='black',lw=5)
tornadoes['MS/square mile'].rolling(window=10,min_periods=1,center=False).mean().plot(color='green',lw=5)
plt.grid()
plt.title('Annual Number of Tornadoes/Square Mile in Oklahoma and Mississippi, 1950-2022',fontsize=16)
plt.xlabel('Year',fontsize=16)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.ylabel('Number of Tornadoes/Square Mile',fontsize=16)
red_patch = Patch(color='red')
blue_patch = Patch(color='blue')
green_patch = Patch(color='green')
black_patch = Patch(color='black')
plt.legend(handles=[red_patch,blue_patch,green_patch,black_patch],labels=['OK/square mile','MS/square mile', 'MS 10 year rolling average','OK 10 year rolling average'])
plt.show()

i = 1950
a = []
while i < 2023:
    a.append(i)
    i += 1

b = list(tornadoes['MS/square mile'])
c = list(tornadoes['OK/square mile'])
analysis1 = linregress(a,b)
analysis2 = linregress(a,c)
print(analysis1)
print('')
print(analysis2)
