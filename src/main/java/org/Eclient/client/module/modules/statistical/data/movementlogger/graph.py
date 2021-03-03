from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os
import numpy as np


def minmaxArr(arr, arr2):
    if (max(arr)) >= (max(arr2)):
        maxnum = (max(arr))
    else:
        maxnum = (max(arr2))

    if (min(arr)) <= (min(arr2)):
        minnum = (min(arr))
    else:
        minnum = (min(arr2))

    return [minnum, maxnum]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x =[]
y =[]
z =[]


with open('C:\\Users\\Zach\\AppData\\Roaming\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\module\\modules\\statistical\\data\\\movementlogger\\'+'movementlogger.txt', 'r') as coordslist:
    for line in coordslist:
        coords = line.split(' ')
        x.append(float(coords[0]))
        y.append(float(coords[1]))
        z.append(float(coords[2]))
print (x)
print (y)
print (z)

# start, end = ax.get_xlim()
# ax.xaxis.set_ticks(np.arange(start, end, 5))
# ax.yaxis.set_ticks(np.arange(start, end, 5))

ax.scatter(x, z, y, c='r', marker='o')

minim = minmaxArr(x, z)[0]
maxim = minmaxArr(x, z)[1]

ax.set_xlim(minim, maxim)
ax.set_zlim(0, 256)
ax.set_ylim(minim, maxim)

ax.set_xlabel('X Label')
ax.set_ylabel('Z Label')
ax.set_zlabel('Y Label')

plt.show()