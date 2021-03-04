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

nocoords = True

with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\module\\modules\\statistical\\data\\\movementlogger\\'+'movementlogger.txt', 'r') as coordslist:
    if nocoords:
        first_line = coordslist.readline()
        coords = first_line.split(' ')
        xcanceloutcoord = abs(float(coords[0]))
        zcanceloutcoord = abs(float(coords[2]))
        for line in coordslist:
            coords = line.split(' ')
            x.append(float(coords[0])+xcanceloutcoord)
            y.append(float(coords[1]))
            z.append(float(coords[2])+zcanceloutcoord)
    else:
        for line in coordslist:
            coords = line.split(' ')
            x.append(float(coords[0]))
            y.append(float(coords[1]))
            z.append(float(coords[2]))


ax.scatter(x, z, y, c='r', marker='o')

minim = minmaxArr(x, z)[0]
maxim = minmaxArr(x, z)[1]

print (minim)
print (maxim)

ax.set_xlim(minim, maxim)
ax.set_zlim(0, max(y))
ax.set_ylim(minim, maxim)

ax.set_xlabel('X Label')
ax.set_ylabel('Z Label')
ax.set_zlabel('Y Label')

plt.show()